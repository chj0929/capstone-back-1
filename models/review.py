
from app import db

class Review(db.Model):
  __tablename__= 'reviews'

  r_id = db.Column(db.Integer, default=0, primary_key=True, autoincrement=True)
  rating = db.Column(db.Float, nullable=False)
  review_txt = db.Column(db.String(50), nullable=False)

  u_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  isbn = db.Column(db.Integer, db.ForeignKey('books.isbn'), nullable=False)
