import jwt
import datetime

from flask import current_app

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
        current_app.config.get('SECRET_KEY'),
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
      payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
      return payload['sub']
    except jwt.ExpiredSignatureError:
      return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
      return 'Invalid token. Please log in again.'