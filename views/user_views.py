from flask import Blueprint, jsonify

from models.user import User

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
def get_my_info():
  return 'Hello, Pybo!'


# @bp.route('/users')
# def get_all_users():
#   queryset = User.query.all()
#
#   if not len(queryset):
#     return ''
#   return jsonify([r.serialize() for r in queryset])


@bp.get('/<int:user_id>')
def get_user_info(user_id):
  print(user_id)
  return 'get_user_info'