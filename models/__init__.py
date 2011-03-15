from mogo import Model, Field, ReferenceField


class User(Model):

    key = Field()
    name = Field()
    email = Field()
    created_at = Field()
    access_token = Field()
    caste = Field()

    def survey_results(self, surveykey):
        return SurveyResponse.search(
            user=self,
            surveykey=surveykey
            ).first()


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

    surveykey = Field()
    user = ReferenceField(User)
    answers = Field()

    def answer(self, key, default=None):
        return self.answers.get(key, default)


