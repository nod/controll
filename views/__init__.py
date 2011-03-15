from tornado_addons.route import route


# must come last, after all views are imported.
routes = route.get_routes()
