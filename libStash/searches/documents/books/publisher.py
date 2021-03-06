from books.models import Publisher
from libStash.settings.base import ELASTICSEARCH_INDEX_NAMES

from django_elasticsearch_dsl import (
    Document,
    Index,
    TextField,
    IntegerField,
    DateField,
)

INDEX = Index(ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class PublisherDocument(Document):
    """Publisher Elasticsearch document"""

    # document fields
    id = IntegerField(attr="id")
    unique_id = TextField()
    name = TextField()
    email = TextField()
    address = TextField()
    publisher_url = TextField()

    class Django(object):
        """The model associate with this Document"""

        model = Publisher