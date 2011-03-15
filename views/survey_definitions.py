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
            options=[('learner','Learner'), ('teacher', 'Teacher')],
            key='pyexp',
            ),
        dict(
            title='How much experience do you have coding other than Python?',
            formtype='radio',
            options=[('little','A little'), ('lot', 'A lot')],
            key='codeother',
            ),
        dict(
            title='Are you interested in staying for a code sprint the next day?',
            formtype='radio',
            options=[('yes','Yes'), ('no', 'No')],
            key='sprint',
            ),


        dict(
            title='Willing to help setup?',
            formtype='radio',
            options=[('yes','Yes'), ('no', 'No')],
            key='setup',
            ),

        dict(
            title="Willing to drive others?",
            formtype='radio',
            options=[('yes','Yes'), ('no', 'No')],
            key='drive',
            ),
        ]
    )

survey_list = [registration, optional]


