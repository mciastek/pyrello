from http import HTTPStatus

from flask import current_app
from itsdangerous import TimestampSigner
from flask_restful import Resource, reqparse

from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('email', help='This field cannot be blank', required = True)

pass_secret = current_app.config.get('PASS_SECRET_KEY')
pass_token_age = current_app.config.get('PASS_TOKEN_AGE')

class Password(Resource):
  def reset(self):
    data = parser.parse_args()
    email = data['email']

    user = User.get_by_email(email)

    if user:
      singed = TimestampSigner(pass_secret)
      token = singed.sign(user.email)
      singed.unsign(token, max_age=pass_token_age)

      # TODO: add sending email
      print(f'Reset password link: password/reset?token={token}')

      return {}, HTTPStatus.NO_CONTENT

    return {
      'message': {
        'email': 'Not found'
      }
    }, HTTPStatus.NOT_FOUND
