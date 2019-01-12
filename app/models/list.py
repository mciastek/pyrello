import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db

class List(db.Model):
  __tablename__ = 'list'

  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.Text, nullable=False)
  position = db.Column(db.Integer, nullable=False, default=1)

  board_id = db.Column(UUID(as_uuid=True), db.ForeignKey('board.id'), nullable=False)
  cards = db.relationship('Card', backref='list', lazy=True)

  def __init__(self, name, position):
    self.name = name
    self.position = position

  def __repr__(self):
    return '<List %r>' % self.name