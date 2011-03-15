
import json
from random import randint
from datetime import datetime

import tornado.web
import tornado.auth

from . import route, BaseHandler, models

@route('/welcome/?')
class Welcome(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('welcome.html')


class NewUserMixin(tornado.web.RequestHandler):

    def new_user(self, uid, name, access_token):
        user = models.User()
        user.key = uid
        user.name = name
        user.access_token = access_token
        user.save()
        self.set_current_user(user)
        self.redirect('/survey/pytx11reg')


@route('/session/destroy/?')
class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_current_user()
        self.redirect('/')


@route('/session/twitter/?', name='auth_twitter')
@route('/session/twitter/after/?', name='auth_twitter_after')
@route('/after/twitter')
class TwitterHandler(BaseHandler, NewUserMixin, tornado.auth.TwitterMixin):

    @tornado.web.asynchronous
    def get(self):
        if not self.get_argument("oauth_token", None):
            self.authorize_redirect()
            return
        self.get_authenticated_user(self._got_authed)

    def _got_authed(self, user_d):
        if not user_d:
            raise tornado.web.HTTPError(500, "Twitter auth failed")
            return

        self.user_d = user_d # save this for later
        uid = 'twit:%s' % (user_d['screen_name'])

        u_ = models.User.search(key=uid).first()
        if u_:
            self.set_current_user(u_)
            u_.access_token = json.dumps(self.user_d['access_token'])
            u_.save()
            self.redirect('/me')
            return
        else:
            name = self.user_d.get('name', self.user_d['screen_name'])
            self.new_user(
                uid,
                name,
                access_token=json.dumps(self.user_d['access_token']),
                )


@route('/session/facebook/?', name='auth_facebook')
@route('/session/facebook/after/?', name='auth_facebook_after')
@route('/after/facebook')
class FacebookHandler(BaseHandler, NewUserMixin, tornado.auth.FacebookGraphMixin):

    @tornado.web.asynchronous
    def get(self):

        my_url = "http://5invites.com/session/facebook/after"

        if self.get_argument("code", False):
            # we've bounced this way before
            self.get_authenticated_user(
                redirect_uri=my_url,
                client_id=self.settings["facebook_api_key"],
                client_secret=self.settings["facebook_secret"],
                code=self.get_argument("code"),
                callback=self.async_callback(self._on_login) )
            return

        self.authorize_redirect(
            redirect_uri=my_url,
            client_id=self.settings["facebook_api_key"],
            extra_params={"scope": "user_about_me,publish_stream"} )

    def _on_login(self, user):
        uid = 'fb:%s' % user['id']
        if u_:
            user_ = models.User(**u_)
            user_.access_token = user['access_token']
            user_.facebook_id = user['id']
            user_.save()
            self.set_current_user(user_)
            self.redirect('/me')
            return
        else:
            name = user.get('name')
            netid = user.get('id')
            self.new_user(uid, name, access_token=user['access_token'])


