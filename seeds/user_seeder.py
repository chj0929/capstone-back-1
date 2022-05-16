from flask_seeder import Seeder, Faker, generator
import bcrypt

from models.user import User




# https://pypi.org/project/Flask-Seeder/
class UserSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 1

  # flask seed run
  def run(self):
    faker = Faker(
      cls=User,
      init={
        "id": generator.Sequence(),
        "email": generator.Email(),
        "password": bcrypt.hashpw('aaa'.encode('utf-8'), bcrypt.gensalt()),
        "nickname": generator.Name(),
        "user_class": "user",
      }
    )

    for user in faker.create(10):
      self.db.session.add(user)

    user1 = User(
      email="aaa@aaa.com",
      password=bcrypt.hashpw('aaa'.encode('utf-8'), bcrypt.gensalt()),
      nickname="aaa"
    )
    self.db.session.add(user1)

  # def run(self):
  #   ######################
  #   ### User
  #   ######################
  #   user1 = User(
  #     email="aaa@aaa.com",
  #     password=bcrypt.hashpw('aaa'.encode('utf-8'), bcrypt.gensalt()),
  #     nickname="aaa"
  #   )
  #   user2 = User(
  #     email="bbb@bbb.com",
  #     password=bcrypt.hashpw('bbb'.encode('utf-8'), bcrypt.gensalt()),
  #     nickname="bbb"
  #   )
  #   self.db.session.add(user1)
  #   self.db.session.add(user2)



















