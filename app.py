import os

from flask import Flask
from sqlalchemy import create_engine
from flask_cors import CORS
from dotenv import load_dotenv


app = Flask(__name__)
PORT=5000

@app.route('/')
def hello_world():
  return 'Hello World!'


if __name__ == '__main__':
  # db
  load_dotenv(verbose=True)
  engine = create_engine(f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@127.0.0.1/{os.getenv("DB_NAME")}')
  connection = engine.connect()

  result = connection.execute("SHOW TABLES;")
  print('result')
  print(result.fetchall())


  app.run('0.0.0.0', port=PORT)
