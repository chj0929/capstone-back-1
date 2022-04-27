from flask import Blueprint, jsonify

from models.user import User


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/')
def get():
  queryset = User.query.all()

  if not len(queryset):
    return ''
  return jsonify([r.serialize() for r in queryset])