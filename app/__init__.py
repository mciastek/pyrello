from flask import Flask
from config import Config
from flask_migrate import Migrate

from app.models import db, bcrypt

migrate = Migrate()

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  migrate.init_app(app, db)
  bcrypt.init_app(app)

  @app.route('/')
  def hello_world():
      return 'Hello, Pyrello!'

  return app