from . import BaseHandler, route


@route('/', name="index")
class Index(BaseHandler):

    def get(self):
        self.render("index.html")
