from flask import Blueprint, jsonify, Response, request

from app import db
from models.book import Book
from utils.auth import login_required

bp = Blueprint('book', __name__, url_prefix='/book')

# TODO: 각 엔드포인트에 login_required 추가

@bp.get('/')
# @login_required
def get_all_books():
  all_books = Book.query.all()
  result = list(map(lambda x: x.serialize(), all_books))
  print(result)
  return jsonify(result)


@bp.get('/<int:book_isbn>')
def get_user_info(book_isbn):
  searching_book = Book.query.filter_by(isbn=book_isbn).first()
  if searching_book is None:
    return Response(status=404)
  return jsonify(searching_book.serialize())


@bp.post('/')
def register_new_book():
  res_dict = request.json


  # if res_dict.get('email') and res_dict.get('password') and res_dict.get('nickname'):

  # isbn = res_dict.get('isbn')
  # title = res_dict.get('title')
  # author = res_dict.get('author')
  # publisher = res_dict.get('publisher')
  # genre = res_dict.get('genre')
  # info = res_dict.get('info')
  # average = res_dict.get('average')
  # count = res_dict.get('count')
  # list_price = res_dict.get('listPrice')
  # price = res_dict.get('price')
  # page = res_dict.get('page')
  # likes = res_dict.get('likes')
  # img_url = res_dict.get('imgUrl')
  #
  # if isbn is None or \
  #   title is None or \
  #   author is None or \
  #   publisher is None or \
  #   genre is None or \
  #   info is None or \
  #   average is None or \
  #   count is None or \
  #   list_price is None or \
  #   price is None or \
  #   page is None or \
  #   likes is None or \
  #   img_url is None:
  #   return Response(status=400)
  #
  # Book(
  #   isbn=isbn,
  #   title=title,
  #   author=author,
  #   publisher=publisher,
  # )

  return 'register_new_book'

# TODO: 수정 엔드포이트 추가

@bp.delete('/<int:book_isbn>')
def delete_book(book_isbn):
  result = Book.query.filter_by(isbn=book_isbn).first()
  if result is None:
    return Response(status=404)
  else:
    db.session.delete(result)
    db.session.commit()
    return Response(status=200)






