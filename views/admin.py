import tornado.web

from . import route, BaseHandler, models


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
        self.render('admin.html', attendees=attendees)


@route('/admin/user/([:a-z0-9\-_]+)', name="admin-user")
class Login(BaseHandler):

    def get(self, userkey):

        user = models.User.search(key=userkey).first()

        self.render('admin_user.html',
            user=models.User.search(key=userkey).first(),
            surveys=models.SurveyResponse.search(user=user),
            Survey = models.Survey,
            )

