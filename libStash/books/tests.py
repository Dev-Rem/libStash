"""Required imports"""
from django.test import TestCase, RequestFactory
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import force_authenticate
from users.models import Account
from .models import (
    Publisher,
    Author,
    Book,
    Warehouse,
    WarehouseBook,
    BookImage,
    BookComment,
    Cart,
    BookInCart,
)

# Create your tests here.


class PublisherTestCase(TestCase):
    """
    Test cases for the Publisher model
    """

    def setUp(self):
        """ Set up data to be used in test cases """

        Publisher.objects.create(
            name="Test Name",
            address="Test address",
            email="testemail@email.com",
            publisher_url="http://testpublisherurl.com",
        )

    def test_model_fields_with_correct_values(self):
        """ Test the model fields with correct values. """

        publisher = Publisher.objects.get(name="Test Name")

        self.assertEqual(publisher.name, "Test Name")
        self.assertEqual(publisher.address, "Test address")
        self.assertEqual(publisher.email, "testemail@email.com")
        self.assertEqual(publisher.publisher_url, "http://testpublisherurl.com")

    def test_model_fields_with_incorrect_values(self):
        """ Test the model fields with incorrect values. """

        publisher = Publisher.objects.get(name="Test Name")

        self.assertNotEqual(publisher.name, "Wrong Test Name")
        self.assertNotEqual(publisher.address, "Wrong Test address")
        self.assertNotEqual(publisher.email, "wrongtestemail@email.com")
        self.assertNotEqual(publisher.publisher_url, "http://wrongtestpublisherurl.com")

    def test_create(self):
        """ Test create functionality on model instance """

        publisher = Publisher.objects.create(
            name="Test Name 2",
            address="Test address 2",
            email="testemail2@email.com",
            publisher_url="http://testpublisherurl2.com",
        )
        self.assertIsInstance(publisher, Publisher)

    def test_update(self):
        """ Test update functionality on model instance """

        publisher = Publisher.objects.get(name="Test Name")
        publisher.name = "Test Name Updated"
        publisher.save()

        self.assertEqual(publisher.name, "Test Name Updated")

    def test_delete(self):
        """ Test delete functionality on model instance """

        publisher = Publisher.objects.get(name="Test Name")
        publisher.delete()

        self.assertRaises(ObjectDoesNotExist)


class AuuthorTestCase(TestCase):
    """
    Test casees for the Author model
    """

    def setUp(self):
        """ Set up data to be used in test cases """

        Author.objects.create(
            name="Test Name",
            email="testemail@email.com",
            address="Test address",
            bio="Test bio",
        )

    def test_model_fields_with_correct_values(self):
        """ Test the model fields with correct values. """

        author = Author.objects.get(name="Test Name")

        self.assertEqual(author.name, "Test Name")
        self.assertEqual(author.email, "testemail@email.com")
        self.assertEqual(author.address, "Test address")
        self.assertEqual(author.bio, "Test bio")

    def test_model_fields_with_incorrect_values(self):
        """ Test the model fields with incorrect values. """

        author = Author.objects.get(name="Test Name")

        self.assertNotEqual(author.name, "Wrong Test Name")
        self.assertNotEqual(author.email, "wrongtestemail@email.com")
        self.assertNotEqual(author.address, "Wrong Test address")
        self.assertNotEqual(author.bio, "Wrong Test bio")

    def test_create(self):
        """ Test create functionality on model instance """

        author = Author.objects.create(
            name="Test Name 2",
            email="testemail2@email.com",
            address="Test address 2",
            bio="Test bio 2",
        )

        self.assertIsInstance(author, Author)

    def test_update(self):
        """ Test update functionality on model instance """

        author = Author.objects.get(name="Test Name")
        author.name = "Test Name Update"
        author.save()

        self.assertEqual(author.name, "Test Name Update")

    def test_delete(self):
        """ Test delete functionality on model instance """

        author = Author.objects.get(name="Test Name")
        author.delete()

        self.assertRaises(ObjectDoesNotExist)
