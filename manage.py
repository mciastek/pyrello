import os
from flask_script import Manager
from flask_migrate import MigrateCommand

from app import migrate, db, create_app

app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def recreate_db():
  db.drop_all()
  db.create_all()
  db.session.commit()

if __name__ == '__main__':
  manager.run()