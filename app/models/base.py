import uuid
import jwt
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app import app

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
  def register(cls):
    db.event.listen(cls, 'before_insert', cls.create_time)
    db.event.listen(cls, 'before_update', cls.update_time)

class JWTMixin(object):
  @classmethod
  def encode_auth_token(cls, user_id):
    try:
      payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
      }
      return jwt.encode(
        payload,
        app.config.get('SECRET_KEY'),
        algorithm='HS256'
      )
    except Exception as e:
      return e

  @staticmethod
  def decode_auth_token(auth_token):
    """
    Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
      payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
      return payload['sub']
    except jwt.ExpiredSignatureError:
      return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
      return 'Invalid token. Please log in again.'