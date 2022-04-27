from app import db


class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  content = db.Column(db.String(100))
  # ForeignKey (테이블명.칼럼명)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
  user = db.relationship('User', backref=db.backref('post_set'))