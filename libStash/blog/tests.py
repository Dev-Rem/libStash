import datetime
Ppostfrom django.test import Client
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
        Account.objects.create(firstname='Wrong Test', lastname='Wrong Test',email='wrongtest@email.com')
        Post.objects.create(title='Test Title', content='Test Content', account=account)
        
    def test_model_fields_with_correct_values(self):
        account = Account.objects.get(firstname='Test')
        post = Post.objects.get(title='Test Title')

        self.assertEqual(post.title, 'Test Title' )
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.account, account)
        self.assertTrue(post.is_active)
    
    def test_model_fields_with_incorrect_values(self):
        account = Account.objects.get(firstname='Wrong Test')
        post = Post.objects.get(title='Test Title')

        self.assertNotEqual(post.title, 'Wrong Test title')
        self.assertNotEqual(post.content, 'Wrong Test content')
        self.assertNotEqual(post.account, account)
        self.assertNotEqual(post.is_active, False)

class PostImageTests(TestCase):
    """
    Test case for testing the fields of the Post image model
    """
    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        post = Post.objects.create(title='Test Title', content='Test Content', account=account)
        PostImage.objects.create(post=post, image='image.jpg')
        Post.objects.create(title='Wrong Test Title', content='Wrong Test Content', account=account)

    def test_model_fields_with_correct_values(self):
        post = Post.objects.get(title='Test Title')
        post_image = PostImage.objects.get(post=post)

        self.assertEqual(post_image.image, 'image.jpg')
        self.assertEqual(post_image.post, post)

    def test_model_fields_with_incorrect_values(self):
        post = Post.objects.get(title='Wrong Test Title')
        post_image = PostImage.objects.get(image='image.jpg')

        self.assertNotEqual(post_image.image, 'Wrong_image.jpg')
        self.assertNotEqual(post_image.post, post)

class PostCommmentTests(TestCase):
    """
    Test case for testing the fields of the Post comment model
    """
    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        post = Post.objects.create(title='Test Title', content='Test Content', account=account)
        PostComment.objects.create(account=account, post=post, comment='Test Comment')
        Post.objects.create(title='Wrong Test Title', content='Wrong Test Content', account=account)
        Account.objects.create(firstname='Wrong Test', lastname='Wrong Test',email='wrongtest@email.com')

    def test_model_fields_with_correct_values(self):
        post = Post.objects.get(title='Test Title')
        comment = PostComment.objects.get(post=post)
        account = Account.objects.get(firstname='Test')

        self.assertEqual(comment.comment, 'Test Comment')
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.account, account)

    def test_model_fields_with_incorrect_values(self):
        post = Post.objects.get(title='Wrong Test Title')
        account = Account.objects.get(firstname='Wrong Test')
        comment = PostComment.objects.get(comment='Test Comment')

        self.assertNotEqual(comment.post, post)
        self.assertNotEqual(comment.comment, 'Wrong Test Comment')
        self.assertNotEqual(comment.account, account)

# class PostListViewTests(TestCase):
#     def test_for_post_listing(self):
        
    