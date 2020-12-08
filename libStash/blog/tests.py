import datetime
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
from rest_framework.test import force_authenticate
from blog.models import Post, PostComment, PostImage
from blog.views import PostListView, PostDetailView
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

    
    def test_model_fields_with_values(self):
        account = Account.objects.get(firstname='Test')
        post = Post.objects.get(title='Test Title')

        self.assertEqual(post.title, 'Test Title' )
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.account, account)
        self.assertTrue(post.is_active)
    
    def test_create(self):
        post = Post.objects.get(title='Test Title')
        self.assertIsInstance(post, Post)

    def test_update(self):
        post = Post.objects.get(title='Test Title')
        post.title = 'Updated Test Title'
        post.save()
        self.assertEqual(post.title, 'Updated Test Title')

    def test_delete(self):
        post = Post.objects.get(title='Test Title')
        post.delete()
        self.assertRaises(ObjectDoesNotExist)

class PostImageTests(TestCase):
    """
    Test case for testing the fields of the Post image model
    """
    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        post = Post.objects.create(title='Test Title', content='Test Content', account=account)
        PostImage.objects.create(post=post, image='image.jpg')
        Post.objects.create(title='Wrong Test Title', content='Wrong Test Content', account=account)

    def test_model_fields_with_values(self):
        post = Post.objects.get(title='Test Title')
        post_image = PostImage.objects.get(post=post)

        self.assertEqual(post_image.image, 'image.jpg')
        self.assertEqual(post_image.post, post)

    def test_create(self):
        post_image = PostImage.objects.get(image='image.jpg')
        self.assertIsInstance(post_image, PostImage)

    def test_update(self):
        post_image = PostImage.objects.get(image='image.jpg')
        post_image.image = 'image2.jpg'
        post_image.save()
        self.assertEqual(post_image.image, 'image2.jpg')

    def test_delete(self):
        post_image = PostImage.objects.get(image='image.jpg')
        post_image.delete()
        self.assertRaises(ObjectDoesNotExist)

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

    def test_model_fields_with_values(self):
        post = Post.objects.get(title='Test Title')
        comment = PostComment.objects.get(post=post)
        account = Account.objects.get(firstname='Test')

        self.assertEqual(comment.comment, 'Test Comment')
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.account, account)

    def test_create(self):
        post_comment = PostComment.objects.get(comment='Test Comment')
        self.assertIsInstance(post_comment, PostComment)

    def test_update(self):
        post_comment = PostComment.objects.get(comment='Test Comment')
        post_comment.comment = 'Test Comment Update'
        post_comment.save()
        self.assertEqual(post_comment.comment, 'Test Comment Update')

    def test_delete(self):
        post_comment = PostComment.objects.get(comment='Test Comment')
        post_comment.delete()
        self.assertRaises(ObjectDoesNotExist)

class PostListViewTests(TestCase):
    """
    This class tests the PostListView
    """
    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        Post.objects.create(title='Test Title', content='Test Content', account=account)
        Post.objects.create(title='Test Title 2', content='Test Content 2', account=account)
        self.factory = RequestFactory()
        self.view = PostListView.as_view()
        self.user = Account.objects.get(firstname='Test')

    def test_status_code(self):
        request = self.factory.get('/api/v1/blog/')
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        request = self.factory.get('/api/v1/blog/')
        request.user = self.user
        response = self.view(request)
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Title 2')

    def test_list_count(self):
        request = self.factory.get('/api/v1/blog/')
        request.user = self.user
        response = self.view(request)
        self.assertContains(response, '"count":2')
    
    def test_list_fields(self):
        request = self.factory.get('/api/v1/blog/')
        request.user = self.user
        response = self.view(request)
        self.assertContains(response, 'unique_id')
        self.assertContains(response, 'title')
        self.assertContains(response, 'content')
        self.assertContains(response, 'date')
        self.assertContains(response, 'likes')

    
    def test_post_http_method_not_allowed(self):
        data = {'title': 'Test Title', 'content': 'Test Content',}
        request = self.factory.post('/api/v1/blog/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 405)
    
    def test_put_http_method_not_allowed(self):
        data = {'title': 'Test Title', 'content': 'Test Content',}
        request = self.factory.put('/api/v1/blog/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 405)
    
    def test_delete_http_method_not_allowed(self):
        data = {'title': 'Test Title', 'content': 'Test Content',}
        request = self.factory.delete('/api/v1/blog/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 405)
    
class PostDetailViewTests(TestCase):

    def setUp(self):
        account = Account.objects.create(firstname='Test', lastname='Test',email='test@email.com')
        Post.objects.create(title='Test Title', content='Test Content', account=account)
        self.factory = RequestFactory()
        self.view = PostDetailView.as_view()
        self.user = Account.objects.get(firstname='Test')

    def test_status_code(self):
        post = Post.objects.get(title='Test Title')
        request = self.factory.get('/api/v1/blog/')
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        post = Post.objects.get(title='Test Title')
        request = self.factory.get('/api/v1/blog/post/')
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertContains(response, 'Test Title')
    
    def test_retrieve_fields(self):
        post = Post.objects.get(title='Test Title')
        request = self.factory.get('/api/v1/blog/post/')
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertContains(response, 'unique_id')
        self.assertContains(response, 'title')
        self.assertContains(response, 'content')
        self.assertContains(response, 'date')
        self.assertContains(response, 'likes')

    def test_post_http_method_not_allowed(self):
        post = Post.objects.get(title='Test Title')
        data = {'title': 'Test Title', 'content': 'Test Content',}
        request = self.factory.post('/api/v1/blog/post/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)
    
    def test_put_http_method_not_allowed(self):
        post = Post.objects.get(title='Test Title')
        data = {'title': 'Test Title', 'content': 'Test Content',}
        request = self.factory.put('/api/v1/blog/post/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)
    
    def test_delete_http_method_not_allowed(self):
        post = Post.objects.get(title='Test Title')
        data = {'title': 'Test Title', 'content': 'Test Content',}
        request = self.factory.delete('/api/v1/blog/post/', data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)
    


    