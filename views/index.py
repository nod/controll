from . import BaseHandler, route


@route('/', name="index")
class Index(BaseHandler):

    def get(self):
        self.write('conTROLL')
