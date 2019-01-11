import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db

class Label(db.Model):
  __tablename__ = 'labels'

  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.Text, nullable=False)
  color = db.Column(db.String(8), nullable=False)

  board_id = db.Column(UUID(as_uuid=True), db.ForeignKey('boards.id'), nullable=False)

  def __init__(self, name, color):
    self.name = name
    self.color = color

  def __repr__(self):
    return '<Label %r>' % self.name