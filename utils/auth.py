from functools import wraps
from flask import request, Response

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    user_id = request.cookies.get('session')

    if user_id is None:
      return Response(status=401)

    return f(*args, **kwargs)

  return decorated_function


def not_login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    user_id = request.cookies.get('session')

    if user_id is not None:
      # 이미 로그인한 상태
      return Response(status=401)

    return f(*args, **kwargs)

  return decorated_function