import json
from http import HTTPStatus

URL = '/api/auth/register'

NEW_USER = dict(
  email = 'joe@doe.com',
  password = 'password123'
)

EXISTING_USER = dict(
  email = 'dummy@test.com',
  password = 'password'
)

CONFLICT_RES = dict(
  message = dict(
    email = 'Already in use'
  )
)

def test_existing_user(app, db):
  response = app.post(
    URL,
    data = json.dumps(EXISTING_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.CONFLICT
  assert json.loads(response.data) == CONFLICT_RES

def test_new_user(app, db):
  print(json.dumps(NEW_USER))
  response = app.post(
    URL,
    data = json.dumps(NEW_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.OK
  assert 'access_token' in json.loads(response.data)
  assert 'refresh_token' in json.loads(response.data)