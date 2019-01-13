import json

def test_valid_params(test_client):
  data = dict(
    email = 'foo@bar.com',
    password = 'password'
  )

  response = test_client.post(
    '/auth',
    data = json.dumps(data),
    content_type = 'application/json'
  )
  assert response.status_code == 200
  assert json.loads(response.data) == data

def test_missing_params(test_client):
  data = dict(
    email = 'foo@bar.com'
  )

  response = test_client.post(
    '/auth',
    data = json.dumps(data),
    content_type = 'application/json'
  )

  error_response_json = dict(
    message = dict(
      password = 'This field cannot be blank'
    )
  )

  assert response.status_code == 400
  assert json.loads(response.data) == error_response_json