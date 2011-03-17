from tornado.web import UIModule
from .. import models
import markdown

class MarkDownPage(UIModule):
    def render(self, key):
        page = None
        if isinstance(key, models.Page):
            page = key
            key = page.key
        else:
            page = models.Page.search(key=key).first()
        if not page:
            return ("""<div class='error'>
                    Page "%s" does not exist.
                    (Create it <a href="/admin/page/%s">here</a>.)
                    </div>""" % (key, key))
        md = markdown.Markdown(safe_mode="replace")
        return (md.convert(page.content))

