import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db

class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  text = db.Column(db.Text, nullable=False)

  def __init__(self, text):
    self.text = text

  def __repr__(self):
    return '<Comment %r>' % self.id