from mogo import Model, Field, ReferenceField


class User(Model):

    key = Field()
    name = Field()
    email = Field()
    created_at = Field()
    access_token = Field()
    caste = Field()

    def survey_results(self, surveykey):
        s_ = Survey.search(key=surveykey).first()
        return SurveyResponse.search(user=self, survey=s_).first()


class Event(Model):

    title = Field()
    start_at = Field()
    descr = Field()


class SessionLocation(Model):

    name = Field()
    descr = Field()


class Session(Model):

    title = Field()
    speaker = ReferenceField(SessionLocation)
    descr = Field()
    tags = Field()
    start_at = Field()
    duration = Field()
    location = ReferenceField(SessionLocation)


class Survey(Model):

    key = Field()
    title = Field()
    questions = Field()


class SurveyResponse(Model):

    survey = ReferenceField(Survey)
    user = ReferenceField(User)
    answers = Field()


