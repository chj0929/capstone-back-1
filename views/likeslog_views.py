from flask import Blueprint, jsonify, Response, session

from app import db
from models.book import Book
from models.likeslog import Likeslog
from utils.auth import login_required
from flask import request

bp = Blueprint('likeslog', __name__, url_prefix='/likeslog')


@bp.get('/')
@login_required
def get_all_likeslog():
  result = Likeslog.query.all()
  all_likeslog = list(map(lambda x: x.serialize(), result))
  return jsonify(all_likeslog)


@bp.get('/<int:user_id>')
@login_required
def get_user_likeslog(user_id):
  # 유저가 찜한 목록을 가져온다.
  # print(type(Likeslog.query)) # flask_sqlalchemy.BaseQuery

  result = Likeslog.query.filter_by(u_id=user_id).all()
  user_likeslog = list(map(lambda x: x.serialize(), result))
  return jsonify(user_likeslog)


@bp.post('/')
@login_required
def toggle_user_likeslog():
  req_dict = request.json

  isbn = req_dict.get('isbn')
  user_id = session.get('userid')

  if isbn is None or user_id is None:
    return Response(status=401)

  # 이전에 찜한 적 있는지 확인
  ex_likeslogs = Likeslog.query.filter_by(isbn=isbn, u_id=user_id).first()
  if ex_likeslogs is not None:
    #  찜하기 해제하기
    db.session.delete(ex_likeslogs)
    db.session.commit()
    return '찜목록 제외 성공', 200

  # 책이 존재한다면
  if Book.query.filter_by(isbn=isbn).one() is not None:
    new_likes_log = Likeslog(isbn=isbn, u_id=user_id)
    db.session.add(new_likes_log)
    db.session.commit()
    return '찜목록 추가 성공', 200
  else:
    # 해당 isbn 존재하지 않음
    return Response(status=404)