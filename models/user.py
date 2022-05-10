from app import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(30))
  password = db.Column(db.String(100))
  nickname = db.Column(db.String(30))
  user_class = db.Column(db.String(10))

  # comment = db.relationship('Comment', backref='user')

  def serialize(self):
    return {
      "id": self.id,
      "name": self.name
    }

# https://riptutorial.com/flask/example/31786/relationships--one-to-many
