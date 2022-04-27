from flask import Flask

from . import main_views, auth_views
# import main_views
# ...


def create_endpoints(app: Flask):
  app.register_blueprint(main_views.bp)
  app.register_blueprint(auth_views.bp)