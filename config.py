import os

class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DB_CONNECTION_URI') or \
    'postgresql://pyrello:pyrello@localhost:5432/pyrello'
  SQLALCHEMY_TRACK_MODIFICATIONS = False