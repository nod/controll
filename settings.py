from os import path
from tornado.web import _O

settings_ = dict(
    debug = False,
    debug_pdb = False,

    httpd_port = 5580,

    cookie_secret = "replace this in local",
    xsrf_cookies = True,

    static_path = path.join(path.dirname(__file__), "static"),
    template_path = path.join(path.dirname(__file__), "templates"),

    twitter_consumer_key = '',
    twitter_consumer_secret = '',

    facebook_api_key = '',
    facebook_secret = '',

    login_url = '/login',

    )
# pull in our local overrides
try:
    from settings_local import settings as settings_local
    settings_.update(settings_local)
except ImportError: pass

# lastly, create our settings object
settings = _O(settings_)
