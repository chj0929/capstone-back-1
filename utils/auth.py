from functools import wraps
from flask import request, Response

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    user_id = request.cookies.get('session')

    if user_id is not None:
      print('로그인한 유저')
    else:
      return Response(status=401)

    return f(*args, **kwargs)

  return decorated_function