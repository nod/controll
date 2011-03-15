from . import BaseHandler, route

@route('/survey/([a-z0-9\-_]+)', name="survey")
class SurveyHandler(BaseHandler):

    def get(self, survey_uid):
        self.render("survey.html")

