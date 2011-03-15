from . import models

registration = models.Survey(
    key = 'pytx11reg',
    title = 'PyTX11 Registration',
    questions = [
        dict(
            title='Are you attending?',
            formtype='radio',
            options=[('yes','Yes'), ('maybe', 'Maybe')],
            key='attending',
            ),
        dict(
            title='How experienced with Python are you?',
            formtype='radio',
            options=[('teacher', 'Teacher'), ('learner','Learner')],
            key='pyexp',
            ),
        ]
    )

survey_list = [registration,]


