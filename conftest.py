import pytest

from config import TestConfig

from app import create_app
from app.models import User, db

@pytest.fixture(scope='module')
def dummy_user():
  user = User(
    email='dummy@test.com',
    first_name='Joe',
    last_name='Doe',
    password='password'
  )
  return user

@pytest.fixture(scope='module')
def test_client():
  flask_app = create_app(TestConfig)

  # Flask provides a way to test your application by exposing the Werkzeug test Client
  # and handling the context locals for you.
  client = flask_app.test_client()

  # Establish an application context before running the tests.
  context = flask_app.app_context()
  context.push()

  yield client  # this is where the testing happens!

  context.pop()


@pytest.fixture(scope='module')
def init_database():
  # Create the database and the database table
  db.create_all()

  # Insert user data
  user = User(
    email='dummy@test.com',
    first_name='Joe',
    last_name='Doe',
    password='password'
  )
  db.session.add(user)

  # Commit the changes for the users
  db.session.commit()

  yield db  # this is where the testing happens!

  db.drop_all()
