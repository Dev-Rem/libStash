from django.test import TestCase
from .models import *

# Create your tests here.

class PublisherModelTest(TestCase):

    def setUp(self):
        Publisher.objects.create(
            name = 'Publisher name',
            address = 'Publisher address',
            email = 'publisher@email.com',
            publisher_url = 'https://publisherurl.com'
        )
        

    def test_publisher_model_fields(self):
        publisher = Publisher.objects.get(id=1)

        self.assertEquals(publisher.name, 'Publisher name')
        self.assertEquals(publisher.address, 'Publisher address')
        self.assertEquals(publisher.email, 'publisher@email.com')
        self.assertEquals(publisher.publisher_url, 'https://publisherurl.com')

class AuthorModelTest(TestCase):
    
    def setUp(self):
        Author.objects.create(
            name = 'Author name',
            email = 'author@email.com',
            address = 'Author address',
        )
        

    def test_author_model_fields(self):
        author = Author.objects.get(id=1)

        self.assertEquals(author.name, 'Author name')
        self.assertEquals(author.address, 'Author address')
        self.assertEquals(author.email, 'author@email.com')

class BookModelTest(TestCase):

    def setUp(self):
        publisher = Publisher.objects.create(
            name = 'Publisher name',
            address = 'Publisher address',
            email = 'publisher@email.com',
            publisher_url = 'https://publisherurl.com'
        )
        author = Author.objects.create(
            name = 'Author name',
            email = 'author@email.com',
            address = 'Author address'
        )
        Book.objects.create(
            title = 'Book title',
            author = author,
            publisher = publisher,
            category  = 'FNSY',
            format = 'PPR-BCK',
            isbn = '1234567890123',
            year = 2000,
            price = 20.0
        )
        
    

    def test_book_model_fields(self):
        publisher = Publisher.objects.get(id=1)
        author = Author.objects.get(id=1)
        book = Book.objects.get(id=1)

        self.assertEquals(book.title, 'Book title')
        self.assertEquals(book.author,author)
        self.assertEquals(book.publisher, publisher)
        self.assertEquals(book.category, 'FNSY')
        self.assertEquals(book.format, 'PPR-BCK')
        self.assertEquals(book.isbn, '1234567890123')
        self.assertEquals(book.year, 2000)
        self.assertEquals(book.price, 20.0)

class ImageModelTest(TestCase):


    def setUp(self):
        publisher = Publisher.objects.create(
            name = 'Publisher name',
            address = 'Publisher address',
            email = 'publisher@email.com',
            publisher_url = 'https://publisherurl.com'
        )
        author = Author.objects.create(
            name = 'Author name',
            email = 'author@email.com',
            address = 'Author address'
        )
        book = Book.objects.create(
            title = 'Book title',
            author = author,
            publisher = publisher,
            category  = 'FNSY',
            format = 'PPR-BCK',
            isbn = '1234567890123',
            year = 2000,
            price = 20.0
        )
        Image.objects.create(
            book = book,
            book_cover = 'book_cover.png'
        )
        

    def test_image_model_fields(self):
        book = Book.objects.get(id=1)
        image = Image.objects.get(id=1)

        self.assertEquals(image.book_cover, 'book_cover.png')
        self.assertEquals(image.book, book)
