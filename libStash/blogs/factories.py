import factory
from faker import Faker

from users.factories import AccountFactory
from blogs.models import Post, PostImage, PostComment
from factory.django import DjangoModelFactory

fake = Faker()
Faker.seed(0)


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    content = fake.paragraph(nb_sentences=5)
    is_active = True
    account = factory.SubFactory(AccountFactory)


class PostImageFactory(DjangoModelFactory):
    class Meta:
        model = PostImage

    post = factory.SubFactory(PostFactory)
    image = factory.django.ImageField(color="blue")


class PostCommentFactory(DjangoModelFactory):
    class Meta:
        model = PostComment

    post = factory.SubFactory(PostFactory)
    comment = factory.Faker("sentence", nb_words=20)
    account = factory.SubFactory(AccountFactory)
