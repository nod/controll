import tornado.web
class BaseHandler(tornado.web.RequestHandler):


    def render_string(self, template, **kwa):

        if not self.application._event:
            ""  # GET EVENT DATA AND MAKE A MODEL

        return super(type(self)).render_string(
            self,
            template,
            event = self.application._event,
            **kwa )

    def clear_current_user(self):
        self.set_secure_cookie(
            'authed_user',
            '',
            )

    def set_current_user(self, user):
        # just the user _id
        self.set_secure_cookie(
            'authed_user',
            json.dumps({'user':user._id}),
            expires_days=3,
            )

    def get_current_user(self):
        # just the user _id
        try:
            u_ = json.loads(self.get_secure_cookie('authed_user'))
            return u_['user']
        except:
            return

    @property
    def authed_user(self):
        if not self._authed_user:
            # not cached, look it up in the database
            self.authed_user = '' # XXX FROM DB D00D
        return self._authed_user

    @authed_user.setter
    def authed_user(self, user):
        self._authed_user = user

    def _handle_request_exception(self, e):
        tornado.web.RequestHandler._handle_request_exception(self,e)
        if self.application.settings.get('debug_pdb'):
            import pdb
            pdb.post_mortem()

    def get_error_html(self, status_code, **kwargs):
        return self.render_string(
            'oops.html',
            txt="Something bad has happened. Perhaps refreshing will fix it?",
            )


