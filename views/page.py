from . import BaseHandler, route
from . import models
import re
from tornado.web import HTTPError, authenticated

@route('/page/([a-z0-9\-_]+)', name="page")
class PageHandler(BaseHandler):

    def get(self, page_key):
        page = models.Page.search(key=page_key).first()
        if not page:
            raise HTTPError(404)
        self.render("page/view.html", page=page)

@route("/admin/pages", name="admin-page-list")
class AdminPageListHandler(BaseHandler):

    def get(self):
        pages = models.Page.find().sort('title')
        error = self.get_argument("error", "")
        self.render("page/list.html", pages=pages, error=error)

    def post(self):
        new_page = self.get_argument("new_page")
        fixed_page = re.sub("[^a-z0-9\-\_\s]", "", new_page.lower())
        fixed_page = re.sub("\s+", "-", fixed_page)
        counter = 0
        inc_fixed_page = fixed_page
        while True:
            # Not the most efficient way to do this... 
            page = models.Page.search(key=inc_fixed_page).first()
            if not page:
                break
            counter += 1
            inc_fixed_page = "%s%s" % (inc_fixed_page, counter)
        page = models.Page(title=new_page,
                           key=fixed_page,
                           content="",
                           tags=[])
        page.save()
        return self.redirect("/admin/page/%s" % fixed_page)

@route("/admin/page/([a-z0-9\-_]+)", name="admin-page")
class AdminPageHandler(BaseHandler):

    def get(self, page_key):
        page = models.Page.search(key=page_key).first()
        if not page:
            page = models.Page()
            page.key = page_key
            page.title = "Untitled Page"
            page.content = ""
            page.tags = []
        message = self.get_argument('message', '')
        self.render("page/edit.html", page=page, message=message)

    def post(self, page_key):
        page = models.Page.search(key=page_key).first()
        if not page:
            page = models.Page(key=page_key)
        title = self.get_argument('title', 'Untitled Page')
        content = self.get_argument('content', "")
        tags = [tag.strip() for tag in 
                self.get_argument('tags', '').split(',')
                if tag.strip()]
        page.content = content
        page.title = title
        page.tags = tags
        page.save()
        self.redirect(self.request.uri+"?message=saved")

@route("/admin/page/([a-z0-9\-_]+)/delete", name="admin-page-delete")
class AdminPageHandler(BaseHandler):

    def post(self, page_key):
        page = models.Page.search(key=page_key).first()
        if not page:
            raise HTTPError(404)
        delete_key = self.get_argument('delete_key')
        if delete_key != page.key:
            raise HTTPError(404)
        page.delete()
        return self.redirect("/admin/pages?message=page_deleted")
