import json
from http import HTTPStatus

URL = '/api/auth/register'

EXITSITNG_USER = dict(
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
    data = json.dumps(EXITSITNG_USER),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.CONFLICT
  assert json.loads(response.data) == CONFLICT_RES