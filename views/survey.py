from . import BaseHandler, route
from . import models
from tornado.web import HTTPError, authenticated

@route('/survey/([a-z0-9\-_]+)', name="survey")
class SurveyHandler(BaseHandler):

    @authenticated
    def get(self, survey_key):
        survey = models.Survey.search(key=survey_key).first()
        if not survey:
            raise HTTPError(404)
        self.render("survey.html", survey=survey)

    @authenticated
    def post(self, survey_key):
        pass
