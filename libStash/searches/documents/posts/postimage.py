"""Required imports"""
from blogs.models import PostImage
from django.conf import settings
from django_elasticsearch_dsl import (
    Document,
    Index,
    TextField,
    IntegerField,
    FileField,
    DateField,
)

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class PostImageDocument(Document):
    """PostImage Elasticsearch document."""

    id = IntegerField(attr="id")
    unique_id = TextField()
    post = TextField(attr="post_indexing")
    image = FileField()
    date = DateField()
    last_update = DateField()

    class Django(object):
        """The model associated with this document"""

        model = PostImage
