from app.models import List

def test_list(test_client):
  list = List(
    name='Some awesome List',
    position=1
  )

  assert list.name == 'Some awesome List'
  assert list.position == 1