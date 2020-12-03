import datetime
from django.test import TestCase
from blog.models import Post, PostComment, PostImage
from users.models import  Account



# Create your tests here.

class PostTestCase(TestCase):
    """
    Test case to testing the fields of the Post model
    """
    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        Post.objects.create(title='Test Title', content='Test Content', account=account)
        
    def test_model_fields(self):
        account = Account.objects.get(firstname='Test')
        post = Post.objects.get(title='Test Title')
        self.assertEqual(post.title, 'Test Title' )
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.account, account)
        self.assertTrue(post.is_active)

class PostImageTestCase(TestCase):
    """
    Test case for testing the fields of the Post image model
    """
    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        post = Post.objects.create(title='Test Title', content='Test Content', account=account)
        PostImage.objects.create(post=post, image='image.jpg')

    def test_model_fields(self):
        post = Post.objects.get(title='Test Title')
        post_image = PostImage.objects.get(post=post)
        self.assertEqual(post_image.image, 'image.jpg')

class PostCommmentTestCase(TestCase):
    """
    Test case for testing the fields of the Post comment model
    """
    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        post = Post.objects.create(title='Test Title', content='Test Content', account=account)
        PostComment.objects.create(account=account, post=post, comment='Test Comment')

    def test_model_fields(self):
        post = Post.objects.get(title='Test Title')
        comment = PostComment.objects.get(post=post)
        self.assertEqual(comment.comment, 'Test Comment')