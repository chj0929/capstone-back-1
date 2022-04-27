from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def get_my_info():
    return 'Hello, Pybo!'