from app import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(30))

  # comment = db.relationship('Comment', backref='user')

  def serialize(self):
    return {
      "id": self.id,
      "name": self.name
    }

# https://riptutorial.com/flask/example/31786/relationships--one-to-many
