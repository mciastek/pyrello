from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def init_db_for(app):
  db = SQLAlchemy(app)
  migrate = Migrate(app, db)