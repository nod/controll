from . import BaseHandler, route
from . import models
from tornado.web import HTTPError, authenticated


def mandate_survey(user, surveykey):
    # make them register
    reg_survey = user.survey_results(surveykey)
    if not reg_survey: return True
    return False



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
