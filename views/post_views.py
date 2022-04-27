from flask import Blueprint, jsonify

from models.post import Post

bp = Blueprint('post', __name__, url_prefix='/post')

