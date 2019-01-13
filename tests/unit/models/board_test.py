from app.models import Board

def test_board(test_client):
  board = Board(
    name='My board',
    slug='my_board'
  )

  assert board.name == 'My board'
  assert board.slug == 'my_board'