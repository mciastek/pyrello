import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import db
from .crud import CRUDMixin

class BaseMixin(CRUDMixin, object):
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
  def register(cls):
    db.event.listen(cls, 'before_insert', cls.create_time)
    db.event.listen(cls, 'before_update', cls.update_time)
