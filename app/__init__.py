from flask import Flask
from config import Config
from flask_migrate import Migrate

from app.models import db, bcrypt
from app.resources import api

migrate = Migrate()

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)
  migrate.init_app(app, db)
  bcrypt.init_app(app)
  api.init_app(app)

  @app.route('/')
  def hello_world():
      return 'Hello, Pyrello!'

  return app