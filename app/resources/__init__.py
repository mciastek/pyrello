from .base import api, jwt
from .auth import Auth

api.add_resource(Auth, '/auth')

__all__ = [
  'api',
  'jwt',
  'Auth'
]