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
            title="What's your zip/postal code?",
            formtype='text',
            key='zip',
            ),
        dict(
            title="What's your email address?",
            formtype='text',
            key='email',
            ),
        dict(
            title='What size shirt?',
            formtype='radio',
            options=[('small', 'Small'), ('med','Medium'),
                ('large','Large'), ('xlarge', 'X-Large'),
                ('xxl', 'XX-Large'),
                ],
            key='shirt',
            ),
        ]
    )


optional = models.Survey(
    key = 'pytx11opt',
    title = 'PyTX11 Survey',
    questions = [
        dict(
            title='How experienced with Python are you?',
            formtype='radio',
            options=[('teacher', 'Teacher'), ('learner','Learner')],
            key='pyexp',
            ),
        dict(
            title=':15 ',
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
        dict(
            title="What's your email address?",
            formtype='text',
            key='email',
            ),
        dict(
            title='What size shirt?',
            formtype='radio',
            options=[('small', 'Small'), ('med','Medium'),
                ('large','Large'), ('xlarge', 'X-Large'),
                ('xxl', 'XX-Large'),
                ],
            key='shirt',
            ),
        ]
    )

survey_list = [registration,]


