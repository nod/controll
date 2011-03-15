import tornado.web

from . import route, BaseHandler, models

from survey import mandate_survey

@route('/me/?', name="me")
class Me(BaseHandler):

    @tornado.web.authenticated
    def get(self):

        surveykey='pytx11reg'
        if mandate_survey(self.current_user, surveykey):
            self.redirect('/survey/' + surveykey)
            return

        self.render('me.html')


@route('/login/?', name="login")
class Login(BaseHandler):

    def get(self):

        self.render('login.html')

