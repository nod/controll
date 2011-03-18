from os import path
from tornado.web import _O

settings_ = dict(
    admins = [ 'twit:nod', 'twit:joshmarshall', 'twit:bradevans137', ],

    debug = False,
    debug_pdb = False,

    httpd_port = 5580,

    cookie_secret = "replace this in local",
    xsrf_cookies = True,

    static_path = path.join(path.dirname(__file__), "static"),
    template_path = path.join(path.dirname(__file__), "templates"),

    twitter_consumer_key = 'cDM0snp8FEaOdr5Ii4IOg',
    twitter_consumer_secret = 'rIumSmLk4dmBpCAa9IZmEO9HnKnOlLeL9BH9Qc5CI',

    facebook_api_key = '',
    facebook_secret = '',

    login_url = '/login',

    )
# pull in our local overrides
try:
    from settings_local import settings_ as settings_local
    settings_.update(settings_local)
except ImportError: pass

# lastly, create our settings object
settings = _O(settings_)
