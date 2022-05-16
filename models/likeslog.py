from app import db


class Likeslog(db.Model):
  __tablename__ = 'likeslogs'

  u_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
  isbn = db.Column(db.Integer, db.ForeignKey('books.isbn'), nullable=False, primary_key=True)

  def serialize(self):
    return {
      "u_id": self.u_id,
      "isbn": self.isbn,
    }