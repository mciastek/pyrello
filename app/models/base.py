import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class BaseMixin(object):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  created_at = db.Column('created_at', db.DateTime, nullable=False)
  updated_at = db.Column('updated_at', db.DateTime, nullable=False)

  @staticmethod
  def create_time(mapper, connection, instance):
    now = datetime.utcnow()
    instance.created_at = now
    instance.updated_at = now

  @staticmethod
  def update_time(mapper, connection, instance):
    now = datetime.utcnow()
    instance.updated_at = now

  @classmethod
  def register(self):
    db.event.listen(self, 'before_insert', self.create_time)
    db.event.listen(self, 'before_update', self.update_time)