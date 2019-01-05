from flask import Flask
from config import Config
from .db import init_db_for

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  init_db_for(app)

  @app.route('/')
  def hello_world():
      return 'Hello, Pyrello!'

  return app