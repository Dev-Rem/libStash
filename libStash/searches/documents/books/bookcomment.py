from books.models import BookComment
from libStash.settings.base import ELASTICSEARCH_INDEX_NAMES
from django_elasticsearch_dsl import (
    Document,
    Index,
    TextField,
    IntegerField,
    fields,
    DateField,
)

# Name of the Elasticsearch index
INDEX = Index(ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)

@INDEX.doc_type
class BookCommentDocument(Document):
    id = IntegerField(attr="id")
    unique_id = TextField()
    book = TextField(attr="book_indexing")
    account = TextField(attr="account_indexing")
    comment = TextField()
    date = DateField()
    last_update = DateField()

    class Django(object):
        """The model associate with this Document"""

        model = BookComment
    