import datetime
from django.test import TestCase
from blog.models import Post, PostComment, PostImage
from users.models import  Account



# Create your tests here.

class PostTestCase(TestCase):
    """
    Test case to test some the fields in the Post model
    """
    def setUp(self):

        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        Post.objects.create(title='Test Title', content='Test Content', account=account )
        

    def test_model_fields(self):
        post = Post.objects.get(title='Test Title')
        self.assertEqual(post.title, 'Test Title' )
        self.assertEqual(post.content, 'Test Content')
        self.assertTrue(post.is_active)
