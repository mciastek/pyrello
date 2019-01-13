from flask_restful import Resource, reqparse
from app.models import db

parser = reqparse.RequestParser()
parser.add_argument('email', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class Auth(Resource):
  def post(self):
    data = parser.parse_args()
    return data