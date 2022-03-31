from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 참고 : https://programmers-sosin.tistory.com/entry/Flask-Flask%EC%97%90%EC%84%9C-SQLAlchemy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-Flask-ORM#Flask%--SQLAlchemy%--%EC%--%A-%EC%B-%--%ED%--%--%EA%B-%B-

class User(db.Model):
  __tablename__ = 'users'
  __table_args__ = {'mysql_collate': 'utf8_general_ci'}


  id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
  email = db.Column(db.String(30))
  nickname = db.Column(db.String(30))
  password = db.Column(db.String(100))
  createdAt = db.Column(db.DateTime)
  updatedAt = db.Column(db.DateTime)
