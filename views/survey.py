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

        response = self.current_user.survey_results(survey_key)
        self.render("survey.html", survey=survey, response=response)

    @authenticated
    def post(self, survey_key):
        survey = models.Survey.search(key=survey_key).first()
        if not survey:
            raise HTTPError(404)

        response = self.current_user.survey_results(survey_key)
        if response:
            response.delete()

        answers = {}
        for question in survey.questions:
            key = question.get('key')
            if not key:
                continue
            answer = self.get_argument(key, None)
            if not answer:
                continue
            answers[key] = answer
        entry = {
            "surveykey": survey_key,
            "user": self.current_user,
            "answers": answers
        }
        response = models.SurveyResponse(**entry)
        response.save()
        self.redirect("/me")
