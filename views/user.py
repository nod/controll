import tornado.web

from . import route, BaseHandler, models

@route('/me/?', name="me")
class Me(BaseHandler):

    @tornado.web.authenticated
    def get(self):

        # make them register
        mandatory_survey = 'pytx11reg'
        reg_survey = self.current_user.survey_results(mandatory_survey)
        print reg_survey
        if not reg_survey:
            self.redirect('/survey/' + mandatory_survey)
            return

        self.render('me.html')


@route('/login/?', name="login")
class Login(BaseHandler):

    def get(self):

        self.render('login.html')

