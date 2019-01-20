from .base import api, api_bp, jwt
from .auth import Auth
from .register import Register

api.add_resource(Auth, '/auth')
api.add_resource(Register, '/auth/register')

__all__ = [
  'api',
  'api_bp',
  'jwt',
  'Auth',
  'Register'
]