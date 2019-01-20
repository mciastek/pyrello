import pytest

from config import TestConfig

from app import create_app
from app.models import User, db as _db

@pytest.fixture(scope='session')
def app(request):
  app = create_app(TestConfig)
  client = app.test_client()

  context = app.app_context()
  context.push()

  def teardown():
    context.pop()

  request.addfinalizer(teardown)
  return client

@pytest.fixture(scope='session')
def db(app, request):
  connection = _db.engine.connect()
  trans = connection.begin()

  _db.create_all()

  def close_db_session():
    trans.rollback()
    _db.drop_all()
    connection.close()

  request.addfinalizer(close_db_session)
  return _db

@pytest.fixture(scope='function')
def session(db, request):
  """Creates a new database session for a test."""
  connection = db.engine.connect()
  transaction = connection.begin()

  options = dict(bind=connection, binds={})
  session = db.create_scoped_session(options=options)

  db.session = session

  def teardown():
    transaction.rollback()
    connection.close()
    session.remove()

  request.addfinalizer(teardown)
  return session

@pytest.fixture(scope='function')
def dummy_user(session):
  user = User(
    email='dummy@test.com',
    password='password'
  )

  session.add(user)
  session.commit()

  return user