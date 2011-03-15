from pymongo.objectid import ObjectId


import tornado.web
class BaseHandler(tornado.web.RequestHandler):


    def render_string(self, template, **kwa):

        if not hasattr(self.application, '_event'):
            self.application._event = None
            ""  # GET EVENT DATA AND MAKE A MODEL

        kwa.setdefault('_event', self.application._event)
        return tornado.web.RequestHandler.render_string(
            self,
            template,
            **kwa
        )

    def clear_current_user(self):
        self.set_secure_cookie(
            'authed_user',
            '',
            )

    def set_current_user(self, user):
        # just the user _id
        self.set_secure_cookie(
            'authed_user',
            json.dumps({'user':str(user.id)}),
            expires_days=3,
            )

    def get_current_user(self):
        # just the user _id
        try:
            u_ = json.loads(self.get_secure_cookie('authed_user'))
            return User.grab(ObjectId(u_['user']))
        except:
            return

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


