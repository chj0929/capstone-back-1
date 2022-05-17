from flask import Blueprint, jsonify, request, session, Response

from app import db
from models.bestseller import Bestseller
from utils.auth import login_required, not_login_required

bp = Blueprint('bestseller', __name__, url_prefix='/bestseller')


@bp.get('/')
# @login_required
def get_all_bestseller():
  result = Bestseller.query.all()
  all_bestseller = list(map(lambda x: x.serialize(), result))
  return jsonify(all_bestseller)


@bp.get('/<int:ranking>')
def get_specified_ranking_bestseller(ranking):
  result = Bestseller.query.filter_by(ranking=ranking).first()
  if result is not None:
    return jsonify(result.serialize())
  else:
    return Response(status=404)


# # TODO: 한꺼번에 bestseller 등록하기
# # csv 파일을 받아서
@bp.post('/')
def update_bestseller_ranking():
  result = request.files['file']
  print(request.files)
  print(result)

  # 모두 삭제

  # 일괄 등록

  return 'update_bestseller_csv'
#

# @bp.delete('/')
# def clear_bestseller():
#   Bestseller.query.delete()
