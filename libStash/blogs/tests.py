from django.core.exceptions import ObjectDoesNotExist
from django.test import RequestFactory, TestCase
from rest_framework.test import force_authenticate
from users.models import Account

from .models import Post, PostComment, PostImage
from .views import PostCommentView, PostDetailView, PostListView

# Create your tests here.


class PostTestCase(TestCase):
    """
    Test casees for the Post model
    """

    def setUp(self):
        """ Set up data to be used in test cases """
        account = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        Post.objects.create(title="Test Title", content="Test Content", account=account)

    def test_model_fields_with_correct_values(self):
        """ Test the model fields with correct values. """
        account = Account.objects.get(firstname="Test")
        post = Post.objects.get(title="Test Title")

        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")
        self.assertEqual(post.account, account)
        self.assertTrue(post.is_active)

    def test_model_fields_with_incorrect_values(self):
        """ Test the model fields with correct values. """
        account = Account.objects.create(
            firstname="Wrong Test",
            lastname="Wrong Test",
            email="wrongtest@email.com",
        )
        post = Post.objects.get(title="Test Title")

        self.assertNotEqual(post.title, "Wrong Test Title")
        self.assertNotEqual(post.content, "Wrong Test Content")
        self.assertNotEqual(post.account, account)
        self.assertNotEqual(post.is_active, False)

    def test_create(self):
        """ Test create on model instance """

        account = Account.objects.get(firstname="Test")
        post = Post.objects.create(
            title="Test Title 2", content="Test Content 2", account=account
        )

        self.assertIsInstance(post, Post)

    def test_update(self):
        """ Test update on model instance """

        post = Post.objects.get(title="Test Title")
        post.title = "Updated Test Title"
        post.save()

        self.assertEqual(post.title, "Updated Test Title")

    def test_delete(self):
        """ Test delete functionality on model instance """

        post = Post.objects.get(title="Test Title")
        post.delete()

        self.assertRaises(ObjectDoesNotExist)


class PostImageTestCase(TestCase):
    """
    Test cases for the PostImage model
    """

    def setUp(self):
        account = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        post = Post.objects.create(
            title="Test Title", content="Test Content", account=account
        )
        PostImage.objects.create(post=post, image="image.jpg")
        Post.objects.create(
            title="Wrong Test Title", content="Wrong Test Content", account=account
        )

    def test_model_fields_with_values(self):
        post = Post.objects.get(title="Test Title")
        post_image = PostImage.objects.get(post=post)

        self.assertEqual(post_image.image, "image.jpg")
        self.assertEqual(post_image.post, post)

    def test_create(self):
        """ Test create on model instance """

        post = Post.objects.get(title="Test Title")
        post_image = PostImage.objects.create(image="image2.jpg", post=post)

        self.assertIsInstance(post_image, PostImage)

    def test_update(self):
        """ Test update functionality on model instance """

        post_image = PostImage.objects.get(image="image.jpg")
        post_image.image = "image2.jpg"
        post_image.save()

        self.assertEqual(post_image.image, "image2.jpg")

    def test_delete(self):
        """ Test delete functionality on model instance """

        post_image = PostImage.objects.get(image="image.jpg")
        post_image.delete()
        self.assertRaises(ObjectDoesNotExist)


class PostCommmentTests(TestCase):
    """
    Test cases for the PostComment model
    """

    def setUp(self):
        """ Set up data to be used in test cases """

        account = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        post = Post.objects.create(
            title="Test Title", content="Test Content", account=account
        )
        PostComment.objects.create(account=account, post=post, comment="Test Comment")
        Post.objects.create(
            title="Wrong Test Title", content="Wrong Test Content", account=account
        )
        Account.objects.create(
            firstname="Wrong Test", lastname="Wrong Test", email="wrongtest@email.com"
        )

    def test_model_fields_with_values(self):
        post = Post.objects.get(title="Test Title")
        comment = PostComment.objects.get(post=post)
        account = Account.objects.get(firstname="Test")

        self.assertEqual(comment.comment, "Test Comment")
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.account, account)

    def test_create(self):
        """ Test create functionality on model instance """

        post = Post.objects.get(title="Test Title")
        post_comment = PostComment.objects.create(comment="Test Comment 2", post=post)

        self.assertIsInstance(post_comment, PostComment)

    def test_update(self):
        """ Test update functionality on model instance """

        post_comment = PostComment.objects.get(comment="Test Comment")
        post_comment.comment = "Test Comment Update"
        post_comment.save()

        self.assertEqual(post_comment.comment, "Test Comment Update")

    def test_delete(self):
        """ Test delete functionality on model instance """

        post_comment = PostComment.objects.get(comment="Test Comment")
        post_comment.delete()

        self.assertRaises(ObjectDoesNotExist)


class PostListViewTests(TestCase):
    """
    This class tests the PostListView
    """

    def setUp(self):
        account = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        Post.objects.create(title="Test Title", content="Test Content", account=account)
        Post.objects.create(
            title="Test Title 2", content="Test Content 2", account=account
        )
        self.factory = RequestFactory()
        self.view = PostListView.as_view()
        self.user = Account.objects.get(firstname="Test")

    def test_status_code(self):
        request = self.factory.get("/api/v1/blog/")
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        request = self.factory.get("/api/v1/blog/")
        request.user = self.user
        response = self.view(request)
        self.assertContains(response, "Test Title")
        self.assertContains(response, "Test Title 2")

    def test_list_count(self):
        request = self.factory.get("/api/v1/blog/")
        request.user = self.user
        response = self.view(request)
        self.assertContains(response, '"count":2')

    def test_list_fields(self):
        request = self.factory.get("/api/v1/blog/")
        request.user = self.user
        response = self.view(request)
        self.assertContains(response, "unique_id")
        self.assertContains(response, "title")
        self.assertContains(response, "content")
        self.assertContains(response, "date")
        self.assertContains(response, "likes")

    def test_post_http_method_not_allowed(self):
        data = {
            "title": "Test Title",
            "content": "Test Content",
        }
        request = self.factory.post("/api/v1/blog/", data, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 405)

    def test_put_http_method_not_allowed(self):
        data = {
            "title": "Test Title",
            "content": "Test Content",
        }
        request = self.factory.put("/api/v1/blog/", data, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 405)

    def test_delete_http_method_not_allowed(self):
        data = {
            "title": "Test Title",
            "content": "Test Content",
        }
        request = self.factory.delete("/api/v1/blog/", data, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 405)


class PostDetailViewTests(TestCase):
    def setUp(self):
        account = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        Post.objects.create(title="Test Title", content="Test Content", account=account)
        self.factory = RequestFactory()
        self.view = PostDetailView.as_view()
        self.user = Account.objects.get(firstname="Test")

    def test_status_code(self):
        post = Post.objects.get(title="Test Title")
        request = self.factory.get("/api/v1/blog/")
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        post = Post.objects.get(title="Test Title")
        request = self.factory.get("/api/v1/blog/post/")
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertContains(response, "Test Title")

    def test_retrieve_fields(self):
        post = Post.objects.get(title="Test Title")
        request = self.factory.get("/api/v1/blog/post/")
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertContains(response, "unique_id")
        self.assertContains(response, "title")
        self.assertContains(response, "content")
        self.assertContains(response, "date")
        self.assertContains(response, "likes")

    def test_post_http_method_not_allowed(self):
        post = Post.objects.get(title="Test Title")
        data = {
            "title": "Test Title",
            "content": "Test Content",
        }
        request = self.factory.post("/api/v1/blog/post/", data, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)

    def test_put_http_method_not_allowed(self):
        post = Post.objects.get(title="Test Title")
        data = {
            "title": "Test Title",
            "content": "Test Content",
        }
        request = self.factory.put("/api/v1/blog/post/", data, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)

    def test_delete_http_method_not_allowed(self):
        post = Post.objects.get(title="Test Title")
        data = {
            "title": "Test Title",
            "content": "Test Content",
        }
        request = self.factory.delete("/api/v1/blog/post/", data, format="json")
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)


class PostCommentViewTests(TestCase):
    """Test class for the PostCommentListView"""

    def setUp(self):
        """Set up variables for tests"""

        account = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        post = Post.objects.create(
            title="Test Title", content="Test Content", account=account
        )
        PostComment.objects.create(post=post, account=account, comment="Comment 1")
        PostComment.objects.create(post=post, account=account, comment="Comment 2")

        self.factory = RequestFactory()
        self.view = PostCommentView.as_view()
        self.user = Account.objects.get(firstname="Test")
        self.post = Post.objects.get(title="Test Title")

    def test_status_code(self):
        """Test status code response from endpoint"""

        post = self.post
        request = self.factory.get(f"post/{post.unique_id}/comments/")
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        """Test list function in PostCommentView"""

        post = self.post
        request = self.factory.get(f"post/{post.unique_id}/comments/")
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertContains(response, "Comment 1")
        self.assertContains(response, "Comment 2")

    def test_create(self):
        """Test the create fucntion in PostCommentView"""

        post = self.post
        request = self.factory.post(
            f"post/{post.unique_id}/comments/",
            {"comment": "Comment 3"},
            format="json",
        )
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 302)

    def test_put_http_method_not_allowed(self):
        """Test PUT method not allowed in PostCommentView"""

        post = self.post
        request = self.factory.put(
            f"post/{post.unique_id}/comments/",
            {"comment": "Comment 1"},
            format="json",
        )
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)

    def test_delete_http_method_not_allowed(self):
        """Test DELETE method not allowed in PostCommentView"""

        post = self.post
        request = self.factory.delete(
            "/api/v1/blog/post/",
            {"comment": "Comment 1"},
            format="json",
        )
        force_authenticate(request, user=self.user)
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 405)


class PostImageView(TestCase):
    """Test class for the PostImageView."""

    def setUp(self):
        """Set up variables for tests"""

        account = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        post = Post.objects.create(
            title="Test Title",
            content="Test Content",
            account=account,
        )
        PostImage.objects.create(post=post, image="tesimage.jpg")

        self.factory = RequestFactory()
        self.view = PostCommentView.as_view()
        self.user = Account.objects.get(firstname="Test")

    def test_retrieve(self):
        """Test the retrieve fucntion in PostImageView"""

        post = Post.objects.get(title="Test Title")
        request = self.factory.get(f"post/{post.unique_id}/images/")
        request.user = self.user
        response = self.view(request, unique_id=post.unique_id)
        self.assertEqual(response.status_code, 200)
