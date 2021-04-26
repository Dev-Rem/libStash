import factory
import datetime

from faker import Faker
from factory import fuzzy
from factory.django import DjangoModelFactory

from users.factories import AdminAccountFactory
from books.models import Publisher, Author, Book, BookImage, BookComment

fake = Faker()
Faker.seed(0)

YEAR_CHOICES = []
for year in range(1980, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((year, year))


class PublisherFactory(DjangoModelFactory):
    class Meta:
        model = Publisher

    name = fake.name()
    address = fake.address()
    email = fake.ascii_safe_email()
    publisher_url = fake.uri()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = fake.name()
    address = fake.address()
    email = fake.ascii_safe_email()
    bio = fake.text(max_nb_chars=2000)


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    publisher = factory.SubFactory(PublisherFactory)
    category = fuzzy.FuzzyChoice(choices=["E-BK", "HD-COVER", "PPR-BACK"])
    format = fuzzy.FuzzyChoice(choices=["THR", "FNSY", "RMCE", "AVTRE"])
    isbn = fake.isbn13()
    price = fake.random_number(digits=2)


class BookImageFactory(DjangoModelFactory):
    class Meta:
        model = BookImage

    book = factory.SubFactory(BookFactory)
    image = factory.django.ImageField(color="green")


class BookCommentFactory(DjangoModelFactory):
    class Meta:
        model = BookComment

    book = factory.SubFactory(BookFactory)
    account = factory.SubFactory(AdminAccountFactory)
    comment = factory.Faker("sentence", nb_words=20)
