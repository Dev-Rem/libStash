from books.models import Author
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
class AuthorDocument(Document):
    """Author Elasticsearch document"""

    # document fields
    id = IntegerField(attr="id")
    unique_id = TextField()
    name = TextField()
    email = TextField()
    address = TextField()
    bio = TextField()
    last_update = DateField()

    class Django(object):
        """The model associate with this Document"""

        model = Author