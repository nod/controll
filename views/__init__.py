from tornado_addons.route import route

from base import BaseHandler
from survey import SurveyHandler

import index

# must come last, after all views are imported.
routes = route.get_routes()
