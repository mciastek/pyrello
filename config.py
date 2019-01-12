import os

class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DB_CONNECTION_URI') or \
    'postgresql://pyrello:pyrello@localhost:5432/pyrello'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  BCRYPT_LOG_ROUNDS = 12
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecret'