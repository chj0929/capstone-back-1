import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


# 전체 구조 참고 : https://www.section.io/engineering-education/flask-database-integration-with-sqlalchemy/#creating-a-model-in-flask

PORT=5000

load_dotenv(verbose=True) # 환경 변수 세팅(.env)
app = Flask(__name__)

# db
db_uri = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'
# 추가 세팅
# 참고 : https://programmers-sosin.tistory.com/entry/Flask-Flask%EC%97%90%EC%84%9C-SQLAlchemy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-Flask-ORM
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 스키마 가져오기 + router 에서 사용하기 위해
import models

db.drop_all()
db.create_all()
db.session.commit() # 실제 적용 시점

# cors 설정
CORS(app)

# router
from router import create_endpoints
create_endpoints(app)


if __name__ == '__main__':
  app.run('0.0.0.0', port=PORT)





