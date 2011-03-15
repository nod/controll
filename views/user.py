import tornado.web

from . import route, BaseHandler, models

@route('/me/?', name="me")
class Me(BaseHandler):

    @tornado.web.authenticated
    def get(self):

        surveykey='pytx11reg'
        if not self.current_user.survey_results(surveykey):
            self.redirect('/survey/' + surveykey)
            return

        self.render('me.html')


@route('/login/?', name="login")
class Login(BaseHandler):

    def get(self):

        self.render('login.html')

