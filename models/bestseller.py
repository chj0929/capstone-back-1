from app import db

class Bestseller(db.Model):
  __tablename__= 'bestsellers'

  ranking = db.Column(db.Integer, default=0, nullable=False, primary_key=True)
  isbn = db.Column(db.Integer, db.ForeignKey('books.isbn'), default=0, nullable=False, primary_key=True)

  def serialize(self):
    return {
      "ranking": self.ranking,
      "isbn": self.isbn
    }