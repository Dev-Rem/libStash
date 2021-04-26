import random
import datetime

from django.db import transaction
from django.core.management.base import BaseCommand

from users.models import Account, Address
from blogs.models import Post, PostImage, PostComment

from users.factories import AccountFactory, AddressFactory, AdminAccountFactory
from blogs.factories import PostFactory, PostImageFactory, PostCommentFactory
from books.factories import (
    BookFactory,
    BookCommentFactory,
    BookImageFactory,
    PublisherFactory,
    AuthorFactory,
)

NUM_POSTS = 100
NUM_BOOKS = 50

MODELS = [
    Account,
    Address,
    PostComment,
    PostImage,
    Post,
]

YEAR_CHOICES = []
for year in range(1980, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((year, year))


class Command(BaseCommand):
    help = "Generate Fake Data"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Deleting old data")
        models = MODELS
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        users = []

        self.stdout.write("Creating admin user...")
        admin_user = AdminAccountFactory()

        self.stdout.write("Creating address...")
        AddressFactory(account=admin_user)

        self.stdout.write("Creating posts...")
        for _ in range(NUM_POSTS):
            post = PostFactory(account=admin_user)
            post.likes.add(admin_user)

            for _ in range(2):
                PostImageFactory(post=post)

            for _ in range(2):
                PostCommentFactory(account=admin_user, post=post)

        author = AuthorFactory()
        publisher = PublisherFactory()
        self.stdout.write("Creating books...")
        for _ in range(NUM_BOOKS):
            book = BookFactory(publisher=publisher)
            book.author.add(author)
            book.year = random.choices(YEAR_CHOICES, k=1)[0]

            for _ in range(2):
                BookImageFactory(book=book)

            for _ in range(2):
                BookCommentFactory(book=book, account=admin_user)
