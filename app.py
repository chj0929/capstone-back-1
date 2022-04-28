import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 전체 구조 참고 : https://wikidocs.net/book/4542

PORT = 5000
db = SQLAlchemy()
migrate = Migrate()


def create_app():
  app = Flask(__name__)

  # db
  load_dotenv(verbose=True)  # 환경 변수 세팅(.env)
  db_uri = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'
  # 추가 세팅
  # 참고 : https://programmers-sosin.tistory.com/entry/Flask-Flask%EC%97%90%EC%84%9C-SQLAlchemy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-Flask-ORM
  app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
  app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.secret_key = os.getenv('SECRET_KEY')

  # 스키마 가져오기 + router 에서 사용하기 위해
  db.init_app(app)
  migrate.init_app(app, db)
  import models

  ######################################################

  CORS(app)

  # view
  from views import create_endpoints
  create_endpoints(app)

  return app
