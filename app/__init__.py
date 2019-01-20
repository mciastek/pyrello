from flask import Flask
from config import Config
from flask_migrate import Migrate

from app.models import db, bcrypt
from app.resources import api_bp, jwt

migrate = Migrate()

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)
  migrate.init_app(app, db)
  bcrypt.init_app(app)
  jwt.init_app(app)

  app.register_blueprint(api_bp, url_prefix='/api')

  @app.route('/')
  def hello_world():
      return 'Hello, Pyrello!'

  return app