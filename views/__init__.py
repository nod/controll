from tornado_addons.route import route

# stupid
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import models
import user
import auth
import index

from base import BaseHandler
from survey import SurveyHandler

# must come last, after all views are imported.
routes = route.get_routes()
