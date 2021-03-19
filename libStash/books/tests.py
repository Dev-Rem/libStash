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


class BookTestCase(TestCase):
    """
    Test casees for the Book model
    """

    def setUp(self):
        """ Set up data to be used in test cases """

        self.author = Author.objects.create(
            name="Test Name",
            email="testemail@email.com",
            address="Test address",
            bio="Test bio",
        )
        self.publisher = publisher = Publisher.objects.create(
            name="Test Name",
            address="Test address",
            email="testemail@email.com",
            publisher_url="http://testpublisherurl.com",
        )

        self.book = Book.objects.create(
            title="Test title",
            publisher=publisher,
            category="THR",
            format="E-BK",
            isbn="1234567890123",
            year=2019,
            price=20,
        )
        self.book.author.add(self.author)

    def test_model_fields_with_correct_values(self):
        """ Test the model fields with correct values. """

        author = Author.objects.get(name="Test Name")
        self.assertEqual(self.book.title, "Test title")
        self.assertEqual(self.book.author.get(pk=author.pk), author)
        self.assertEqual(self.book.publisher, self.publisher)
        self.assertEqual(self.book.category, "THR")
        self.assertEqual(self.book.format, "E-BK")
        self.assertEqual(self.book.isbn, "1234567890123")
        self.assertEqual(self.book.year, 2019)
        self.assertEqual(self.book.price, 20)

    def test_model_fields_with_incorrect_values(self):
        """ Test the model fields with incorrect values. """

        wrong_author = Author.objects.create(
            name=" Wrong Test Name",
            email="wrongtestemail@email.com",
            address="Wrong Test address",
            bio="Wrong Test bio",
        )
        wrong_publisher = Publisher.objects.create(
            name="Wrong Test Name",
            address="Wrong Test address",
            email="wrongtestemail@email.com",
            publisher_url="http://wrongtestpublisherurl.com",
        )

        self.assertNotEqual(self.book.title, "Wrong Test title")
        self.assertNotEqual(self.book.author.get(pk=self.author.pk), wrong_author)
        self.assertNotEqual(self.book.publisher, wrong_publisher)
        self.assertNotEqual(self.book.format, "PPR-BCK")
        self.assertNotEqual(self.book.category, "FNSY")
        self.assertNotEqual(self.book.isbn, "1345624539872")
        self.assertNotEqual(self.book.year, 2022)
        self.assertNotEqual(self.book.price, 0)

    def test_create(self):
        """ Test create functionality on model instance """

        book = Book.objects.create(
            title="Test title 2",
            publisher=self.publisher,
            category="THR",
            format="E-BK",
            isbn="1234567890123",
            year=2019,
            price=20,
        )
        book.author.add(self.author)

        self.assertIsInstance(book, Book)

    def test_update(self):
        """ Test update functionality on model instance """

        book = self.book
        book.title = "Update Test Title"
        book.save()

        self.assertEqual(book.title, "Update Test Title")

    def test_delete(self):
        """ Test delete functionality on model instance """

        publisher = Publisher.objects.get(name="Test Name")
        publisher.delete()

        self.assertRaises(ObjectDoesNotExist)


class WarehouseTestCase(TestCase):
    """
    Test casees for the Warehouse model
    """

    def setUp(self):
        """ Set up data to be used in test cases """

        self.warehouse = Warehouse.objects.create(
            address="Test address",
            phone="+36735454656",
        )

    def test_model_fields_with_correct_values(self):
        """ Test the model fields with correct values. """

        self.assertEqual(self.warehouse.address, "Test address")
        self.assertEqual(self.warehouse.phone, "+36735454656")

    def test_model_fields_with_incorrect_values(self):
        """ Test the model fields with incorrect values. """

        self.assertNotEqual(self.warehouse.address, "Wrong Test address")
        self.assertNotEqual(self.warehouse.phone, "+3435342322343")

    def test_create(self):
        """ Test create on model instance """

        self.assertIsInstance(self.warehouse, Warehouse)

    def test_update(self):
        """ Test update on model instance """

        warehouse = self.warehouse
        warehouse.address = "Update Test address"
        warehouse.save()

        self.assertEqual(self.warehouse.address, "Update Test address")

    def test_delete(self):
        """ Test delete functionality on model instance """

        warehouse = Warehouse.objects.get(address="Test address")
        warehouse.delete()

        self.assertRaises(ObjectDoesNotExist)


class WarehouseBookTestCase(TestCase):
    """
    Test casees for the WarehouseBook model
    """

    def setUp(self):
        """ Set up data to be used in test cases """

        self.author = Author.objects.create(
            name="Test Name",
            email="testemail@email.com",
            address="Test address",
            bio="Test bio",
        )
        self.publisher = publisher = Publisher.objects.create(
            name="Test Name",
            address="Test address",
            email="testemail@email.com",
            publisher_url="http://testpublisherurl.com",
        )

        self.book = Book.objects.create(
            title="Test title",
            publisher=publisher,
            category="THR",
            format="E-BK",
            isbn="1234567890123",
            year=2019,
            price=20,
        )
        self.book.author.add(self.author)
        self.warehouse = Warehouse.objects.get(
            address="Test address",
            phone="+345342432",
        )
        self.warehouse_book = WarehouseBook.objects.create(
            warehouse=self.warehouse,
            book=self.book,
            count=2,
        )

    def test_model_fields_with_correct_values(self):
        """ Test the model fields with correct values. """

        self.assertEqual(self.warehouse_book.warehouse, self.warehouse)
        self.assertEqual(self.warehouse_book.book, self.book)
        self.assertEqual(self.warehouse.count, 2)

    def test_model_fields_with_incorrect_values(self):
        """ Test the model fields with correct values. """

        book = Book.objects.create(
            title="Wrong Test title",
            publisher=self.publisher,
            category="THR",
            format="E-BK",
            isbn="1234567890123",
            year=2019,
            price=20,
        )
        book.author.add(self.author)
        warehouse = Warehouse.objects.get(
            address="Test address",
            phone="+345342432",
        )

        self.assertNotEqual(self.warehouse_book.warehouse, self.warehouse)
        self.assertNotEqual(self.warehouse_book.book, book)
        self.assertNotEqual(self.warehouse_book.count, 3)

    def test_create(self):
        """ Test create on model instance """

        self.assertIsInstance(self.warehouse_book, WarehouseBook)

    def test_update(self):
        """ Test update on model instance """

        warehouse_book = self.warehouse_book
        warehouse_book.count = 5
        warehouse_book.save()

        self.assertEqual(warehouse.count, 5)

    def test_delete(self):
        """ Test delete functionality on model instance """

        warehouse_book = self.warehouse_book
        warehouse_book.delete()

        self.assertRaises(ObjectDoesNotExist)
