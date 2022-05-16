from flask_seeder import Seeder

from models.bestseller import Bestseller


class BestsellerSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 3

  def run(self):
    ######################
    ### Bestseller
    ######################
    # isbn 없는 값이면 에러
    best1 = Bestseller(ranking=1, isbn=1)
    best2 = Bestseller(ranking=2, isbn=2)

    self.db.session.add(best1)
    self.db.session.add(best2)