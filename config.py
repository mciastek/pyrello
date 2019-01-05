import os

class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DB_CONNECTION_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = False