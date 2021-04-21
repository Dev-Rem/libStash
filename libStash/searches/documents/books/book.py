from books.models import Book
from libStash.settings.base import ELASTICSEARCH_INDEX_NAMES

from django_elasticsearch_dsl import (
    Document,
    Index,
    TextField,
    IntegerField,
    DateField,
    ObjectField,
    FileField,
)

INDEX = Index(ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class BookDocument(Document):
    id = IntegerField(attr="id")
    unique_id = TextField()
    title = TextField()
    isbn = TextField()
    year = IntegerField()
    price = IntegerField()
    last_update = DateField()
    bookImage = ObjectField(
        properties={
            "id": IntegerField(attr="id"),
            "unique_id": TextField(),
            "book": TextField(attr="book_indexing"),
            "image": FileField(),
            "last_update": DateField(),
        }
    )
    bookComment = ObjectField(
        properties={
            "id": IntegerField(attr="id"),
            "unique_id": TextField(),
            "book": TextField(attr="book_indexing"),
            "account": TextField(attr="account_indexing"),
            "comment": TextField(),
            "date": DateField(),
            "last_update": DateField(),
        }
    )
    author = ObjectField(
        properties={
            "id": IntegerField(attr="id"),
            "unique_id": TextField(),
            "name": TextField(),
            "email": TextField(),
            "address": TextField(),
            "bio": TextField(),
            "last_update": DateField(),
        }
    )
    publisher = ObjectField(
        properties={
            "id": IntegerField(attr="id"),
            "unique_id": TextField(),
            "name": TextField(),
            "email": TextField(),
            "address": TextField(),
            "publisher_url": TextField(),
        }
    )

    class Django(object):
        """The model associate with this Document"""

        model = Book