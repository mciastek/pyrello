import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import db

class Board(db.Model):
  __tablename__ = 'board'

  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.Text, nullable=False)
  slug = db.Column(db.Text, unique=True, nullable=False)

  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
  lists = db.relationship('List', backref='board', lazy=True)
  labels = db.relationship('Label', backref='board', lazy=True)
  cards = db.relationship('Card', backref='board', lazy=True)

  def __init__(self, name, slug):
    self.name = name
    self.slug = slug

  def __repr__(self):
    return '<Board %r>' % self.name