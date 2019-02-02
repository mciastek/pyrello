import json
from http import HTTPStatus

URL = '/api/boards'

def test_forbidden(app, db, dummy_user):
  data = {
    'name': 'Some board',
    'owner_id': dummy_user.id.__str__()
  }

  response = app.post(
    URL,
    data = json.dumps(data),
    content_type = 'application/json'
  )

  assert response.status_code == HTTPStatus.UNAUTHORIZED