from flask_seeder import Seeder

from models.review import Review


class ReviewSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 4

  def run(self):
    ######################
    ### Review
    ######################
    review1 = Review(rating=2.0, review_txt="별로인듯...", u_id=1, isbn=1)
    review2 = Review(rating=4.0, review_txt="인생 책입니다!!!", u_id=2, isbn=2)
    self.db.session.add(review1)
    self.db.session.add(review2)