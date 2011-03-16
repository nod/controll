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

        # we'll get this cursor once, so just pull it all into memory
        attendees_ = models.User.find()

        shirts = {}
        attendees = []
        for a in attendees_:
            attendees.append(a)
            s = a.survey_results('pytx11reg')
            shirts[s.answers['shirt']] = shirts.get(s.answers['shirt'],0) + 1

        lbls = shirts.keys()
        values = [str(shirts[x]) for x in lbls]
        lbls = [ "%s+%0.0f%%" % (L, (shirts[L]/sum(shirts.values()))*100) for L in lbls]
        charts = ( 
            ('pytx11reg', 'attending'),
            ('pxtx11reg','shirt'),
            )
        self.render('admin.html', attendees=attendees, charts=charts)


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

