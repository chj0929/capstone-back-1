import json

from flask import Blueprint, jsonify, request, session, Response
import bcrypt

from app import db
from models.user import User
from utils.auth import login_required, not_login_required

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.post('/signup')
@not_login_required
def signup():
  req_dict = request.json

  if req_dict.get('email') and req_dict.get('password') and req_dict.get('nickname'):
    print(req_dict.get('pw'))

    # gensalt 기본값 10 높아질수록 검증 시간 늘어남.
    encrypted = bcrypt.hashpw(req_dict.get('password').encode('utf-8'), bcrypt.gensalt())
    new_user = User(email=req_dict.get('email'), password=encrypted, nickname=req_dict.get('nickname'))
    db.session.add(new_user)
    db.session.commit()

    return 'login success'
  else:
    # Bad Request
    return Response(status=400)


@bp.post('/login')
@not_login_required
def login():
  credential = request.json
  email = credential['email']
  password = credential['password']

  print(email, password)

  if email != '' and password != '':
    user = User.query.filter_by(email=email).first()

    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
      print('로그인 성공')
      session['userid'] = user.id
      print(session)
      return 'ok'
  return Response(json.dumps({'message': '로그인 실패'}), status=401)




@bp.post('/logout')
@login_required
def logout():
    session.clear()
    return 'logout success', 200