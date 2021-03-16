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
    Test case for the Publisher model
    """

    def setUp(self):
        """ Set up data to be used for testing """
        account_1 = Account.objects.create(
            firstname="Test", lastname="Test", email="test@email.com"
        )
        account_2 = Account.objects.create(
            firstname="Wrong Test", lastname="Wrong Test", email="wrongtest@email.com"
        )
        Publisher.objects.create(
            name="Test Name",
            address="Test address",
            email="testemail@email.com",
            publisher_url="http://testpublisherurl.com",
        )

    def test_model_fields_with_correct_values(self):
        publisher = Publisher.objects.get(name="Test Name")

        self.assertEqual(publisher.name, "Test Name")
        self.assertEqual(publisher.address, "Test address")
        self.assertEqual(publisher.email, "testemail@email.com")
        self.assertEqual(publisher.publisher_url, "http://testpublisherurl.com")
