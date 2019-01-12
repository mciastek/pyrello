import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property

from .base import db, bcrypt, BaseMixin

boards = db.Table('user_board',
  db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True),
  db.Column('board_id', UUID(as_uuid=True), db.ForeignKey('board.id'), primary_key=True)
)

cards = db.Table('user_card',
  db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True),
  db.Column('card_id', UUID(as_uuid=True), db.ForeignKey('card.id'), primary_key=True)
)

class User(BaseMixin, db.Model):
  __tablename__ = 'user'

  first_name = db.Column(db.Text, nullable=False)
  last_name = db.Column(db.Text, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  _password = db.Column(db.String(128))
  created_at = db.Column(db.DateTime, default=db.func.now())
  updated_at = db.Column(db.DateTime, default=db.func.now())

  comments = db.relationship('Comment', backref='author', lazy=True)
  owned_boards = db.relationship('Board', backref='owner', lazy=True)
  owned_cards = db.relationship('Card', backref='owner', lazy=True)

  boards = db.relationship('Board', secondary=boards, lazy='subquery',
    backref=db.backref('user', lazy=True))

  cards = db.relationship('Card', secondary=cards, lazy='subquery',
    backref=db.backref('user', lazy=True))

  def __init__(self, first_name, last_name, email, password):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password

  def __repr__(self):
    return '<User %r>' % self.email

  @hybrid_property
  def password(self):
    return self._password

  @password.setter
  def password(self, plaintext):
    self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')