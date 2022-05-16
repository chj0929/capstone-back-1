from flask_seeder import Seeder

from models.book import Book


class BookSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 0

  def run(self):
    ######################
    ### Book
    ######################
    book1 = Book(isbn=1, title="book1", author="author1", publisher="", genre="", info="", average=4.0, count=0, list_price=0, price=10000, page=150, img_url="" )
    book2 = Book(isbn=2, title="book2", author="author2", publisher="", genre="", info="", average=4.0, count=0, list_price=0, price=20000, page=250, img_url="" )
    self.db.session.add(book1)
    self.db.session.add(book2)

    # 미리 반영해야하는듯
    self.db.session.commit()

