from flask_seeder import Seeder

from models.likeslog import Likeslog


class LikeslogSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 4

  def run(self):
    ######################
    ### Likeslog
    ######################
    # isbn 없는 값이면 에러
    likeslog1 = Likeslog(u_id=1, isbn=1)
    likeslog2 = Likeslog(u_id=2, isbn=2)

    self.db.session.add(likeslog1)
    self.db.session.add(likeslog2)