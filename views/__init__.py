from flask import Flask

from . import main_views, auth_views, user_views, bestseller_views, book_views, likeslog_views


# from . import post_views




def create_endpoints(app: Flask):
  app.register_blueprint(main_views.bp)
  app.register_blueprint(auth_views.bp)
  app.register_blueprint(user_views.bp)
  app.register_blueprint(book_views.bp)
  app.register_blueprint(bestseller_views.bp)
  app.register_blueprint(likeslog_views.bp)

  # app.register_blueprint(post_views.bp)
