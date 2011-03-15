import tornado.web

from . import route, BaseHandler, models

import json

@route('/admin/?', name="admin")
class Admin(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        admins = [
            'twit:nod', 'twit:joshmarshall',
            'twit:bradevans137',
            ]
        if self.current_user.key not in admins:
            self.render('oops.html', txt='bad dog. no donut.')
            return
        attendees = models.User.find()

        shirts = {}
        for a in attendees:
            s = a.survey_results('pytx11reg')
            shirts[s.answers['shirt']] = shirts.get(s.answers['shirt'],0) + 1

        self.render('admin.html', attendees=attendees, shirts=shirts)


@route('/admin/user/([:a-z0-9\-_]+)', name="admin-user")
class Login(BaseHandler):

    def get(self, userkey):

        user = models.User.search(key=userkey).first()

        if self.get_argument('json',False):
            self.write(json.dumps(
                [s.answers for s in models.SurveyResponse.search(user=user) ]
                ))
            return

        self.render('admin_user.html',
            user=models.User.search(key=userkey).first(),
            surveys=models.SurveyResponse.search(user=user),
            Survey = models.Survey,
            )

