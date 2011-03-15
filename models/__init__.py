from mogo import Model, Field, ReferenceField


class User(Model):

    key = Field()
    name = Field()
    created_at = Field()
    access_token = Field()
    caste = Field()


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


