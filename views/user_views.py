from flask import Blueprint, jsonify, Response

from models.user import User
from utils.auth import login_required
from flask import request

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.get('/')
@login_required
def get_my_info():
  print(request.cookies.get('session'))
  return 'ok'


@bp.route('/users')
def get_all_users():
  queryset = User.query.all()

  if not len(queryset):
    return Response(status=404)
  return jsonify([r.serialize() for r in queryset])


@bp.get('/<int:user_id>')
def get_user_info(user_id):
  print(user_id)
  return 'get_user_info'

