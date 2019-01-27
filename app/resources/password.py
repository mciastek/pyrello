from http import HTTPStatus

from flask import current_app, request, make_response, jsonify
from itsdangerous import TimestampSigner

from .base import api_bp
from app.models import User

@api_bp.route('/password/send', methods=['POST'])
def send():
  pass_secret = current_app.config.get('PASS_SECRET_KEY')
  pass_token_age = current_app.config.get('PASS_TOKEN_AGE')
  email = request.json.get('email')

  user = User.get_by_email(email)

  if user:
    singed = TimestampSigner(pass_secret)
    token = singed.sign(user.email)
    singed.unsign(token, max_age=pass_token_age)

    # TODO: add sending email
    print(f'Reset password link: /password/reset?token={token}'.encode('utf-8'))

    return make_response(
      jsonify({
        'message': 'Email has been sent'
      }),
      HTTPStatus.ACCEPTED
    )

  return make_response(
    jsonify({
      'message': {
        'email': 'Not found'
      }
    }),
    HTTPStatus.NOT_FOUND
  )
