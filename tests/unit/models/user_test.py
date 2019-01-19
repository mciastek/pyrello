from app.models import User

def test_user(app):
  user = User(
    first_name='Bruce',
    last_name='Wright',
    email='bruce@wright.com',
    password='password123'
  )

  assert user.first_name == 'Bruce'
  assert user.last_name == 'Wright'
  assert user.email == 'bruce@wright.com'
  assert user._password != 'password123'