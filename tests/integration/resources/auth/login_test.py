import json
from http import HTTPStatus

URL = '/api/auth'

VALID_USER = dict(
  email = 'dummy@test.com',
  password = 'password'
)

INVALID_USER = dict(
  email = 'foo@bar.com',
  password = 'password'
)

INVALID_CREDENTIALS_RES = dict(
  message = 'Invalid credentials'
)

def test_invalid_email(app, db):
  response = app.post(
    URL,
    data = json.dumps(INVALID_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.FORBIDDEN
  assert json.loads(response.data) == INVALID_CREDENTIALS_RES

def test_invalid_password(app, db):
  data = dict(
    email = VALID_USER['email'],
    password = 'invalid password'
  )

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.FORBIDDEN
  assert json.loads(response.data) == INVALID_CREDENTIALS_RES


def test_missing_params(app, db):
  data = dict(
    email = INVALID_USER['email']
  )

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  error_response_json = dict(
    message = dict(
      password = 'This field cannot be blank'
    )
  )

  assert response.status_code == HTTPStatus.BAD_REQUEST
  assert json.loads(response.data) == error_response_json

def test_valid_credentials(app, db):
  response = app.post(
    URL,
    data = json.dumps(VALID_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.OK
  assert 'access_token' in json.loads(response.data)
  assert 'refresh_token' in json.loads(response.data)