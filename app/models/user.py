import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  first_name = db.Column(db.Text, nullable=False)
  last_name = db.Column(db.Text, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  _password = db.Column(db.String(128))

  def __init__(self, first_name, last_name, email):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email

  def __repr__(self):
    return '<User %r>' % self.email

  @hybrid_property
  def password(self):
    return self._password

  @password.setter
  def _set_password(self, plaintext):
    self._password = bcrypt.generate_password_hash(plaintext)