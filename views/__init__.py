from tornado_addons.route import route

from base import BaseHandler

# stupid
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import models

import auth
import index

# must come last, after all views are imported.
routes = route.get_routes()
