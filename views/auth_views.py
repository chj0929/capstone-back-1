import json

from flask import Blueprint, jsonify, request, session
import bcrypt

from app import db
from models.user import User
from utils.auth import login_required, not_login_required

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.post('/signup')
@not_login_required
def signup():
  res_dict = request.json

  if res_dict.get('email') and res_dict.get('password') and res_dict.get('nickname'):
    print(res_dict.get('pw'))

    # gensalt 기본값 10 높아질수록 검증 시간 늘어남.
    encrypted = bcrypt.hashpw(res_dict.get('password').encode('utf-8'), bcrypt.gensalt())
    new_user = User(email=res_dict.get('email'), password=encrypted, nickname=res_dict.get('nickname'))
    db.session.add(new_user)
    db.session.commit()

    return '회원 가입 성공'
  else:
    return '입력 누락!!!'


@bp.post('/login')
@not_login_required
def login():
  credential = request.json
  email = credential['email']
  password = credential['password']

  print(email, password)


  # res_dict = request.args.to_dict()
  # if res_dict.get('email') and res_dict.get('password'):
  if email != '' and password != '':
    user = User.query.filter_by(email=email).first()

    #

    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
      print('로그인 성공')
      session['userid'] = user.id
      print(session)
      return 'ok'
    else:
      return '비밀번호 틀림'
  else:
    return '로그인 실패', 401



@bp.post('/logout')
@login_required
def logout():
    session.clear()
    return 'logout success'