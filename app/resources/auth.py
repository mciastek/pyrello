from flask_restful import Resource, reqparse
from flask_jwt_extended import (
  create_access_token,
  create_refresh_token,
  jwt_required,
  jwt_refresh_token_required,
  get_jwt_identity,
  get_raw_jwt
)

from app.models import User, db

parser = reqparse.RequestParser()
parser.add_argument('email', help='This field cannot be blank', required = True)
parser.add_argument('password', help='This field cannot be blank', required = True)

class Auth(Resource):
  def post(self):
    data = parser.parse_args()
    email = data['email']
    password = data['password']
    current_user = User.get_by_email(email)

    if not current_user:
      return { 'message': f'User {email} doesn\'t exist!' }, 404

    if current_user.password_match(password):
      access_token = create_access_token(identity=email)
      refresh_token = create_refresh_token(identity=email)

      return {
        'access_token': access_token,
        'refresh_token': refresh_token
      }

    return { 'messsage': 'Wrong credentials' }, 403