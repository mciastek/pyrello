import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db

class Card(db.Model):
  __tablename__ = 'cards'

  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text, nullable=False)
  position = db.Column(db.Integer, nullable=False, default=1)
  comments = db.relationship('Comment', backref='card', lazy=True)

  def __init__(self, name, description, position):
    self.name = name
    self.description = description
    self.position = position

  def __repr__(self):
    return '<Card %r>' % self.name