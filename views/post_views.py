from flask import Blueprint, jsonify, request, Response

from app import db
from models.post import Post

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.get('/')
def get_all_posts():
  posts = Post.query.all()
  return jsonify(posts)


@bp.post('/')
def create_post():
  created_info = request.json
  print(created_info)
  content = created_info.get('content')
  user_id = created_info.get('userId')

  if user_id is not None and content is not None:
    new_post = Post(content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    print(new_post)

    return Response(status=201)
  else:
    return Response(status=400)


