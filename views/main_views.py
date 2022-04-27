from flask import Blueprint

from utils.auth import login_required

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
@login_required
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'