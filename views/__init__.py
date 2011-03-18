from tornado_addons.route import route

# stupid
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import models
from base import BaseHandler, requires_admin

import user
import auth
import index
import survey
import admin
import page

# must come last, after all views are imported.
routes = route.get_routes()
