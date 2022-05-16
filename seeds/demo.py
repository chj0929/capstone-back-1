from flask_seeder import Seeder, Faker, generator
import bcrypt

from models.user import User



# https://pypi.org/project/Flask-Seeder/
class DemoSeeder(Seeder):
  def run(self):
    faker = Faker(
      cls=User,
      init={
        "id": generator.Sequence(start=5),
        "email": generator.Email(),
        "password": bcrypt.hashpw('ddd'.encode('utf-8'), bcrypt.gensalt()),
        "nickname": generator.Name(),
        "user_class": "user",
      }
    )

    for user in faker.create(2):
      self.db.session.add(user)