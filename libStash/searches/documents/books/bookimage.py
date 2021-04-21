from books.models import BookImage
from libStash.settings.base import ELASTICSEARCH_INDEX_NAMES
from django_elasticsearch_dsl import (
    Document,
    Index,
    TextField,
    IntegerField,
    FileField,
    DateField,
)

# Name of the Elasticsearch index
INDEX = Index(ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class BookImageDocument(Document):
    """BookImage Elasticsearch document"""

    # document fields
    id = IntegerField(attr="id")
    unique_id = TextField()
    book = TextField(attr="book_indexing")
    image = FileField()

    class Django(object):
        """The model associate with this Document"""

        model = BookImage