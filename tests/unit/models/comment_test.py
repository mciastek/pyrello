from app.models import Comment

def test_comment(test_client):
  comment = Comment(
    text='Some awesome comment'
  )

  assert comment.text == 'Some awesome comment'