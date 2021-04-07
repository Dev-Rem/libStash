"""Required imports"""
from blogs.models import Post, PostImage, PostComment
from django.conf import settings
from django_elasticsearch_dsl import (
    Document,
    Index,
    TextField,
    IntegerField,
    DateField,
    BooleanField,
    ObjectField,
    FileField,
)

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
class PostDocument(Document):
    """Post Elasticsearch document."""

    # document fields
    id = IntegerField(attr="id")
    unique_id = TextField()
    title = TextField()
    content = TextField()
    date = DateField()
    is_active = BooleanField()
    last_update = DateField()
    postImage = ObjectField(
        properties={
            "id": IntegerField(attr="id"),
            "unique_id": TextField(),
            "post": TextField(attr="post_indexing"),
            "image": FileField(),
            "date": DateField(),
            "last_update": DateField(),
        }
    )
    postComment = ObjectField(
        properties={
            "id": IntegerField(attr="id"),
            "unique_id": TextField(),
            "post": TextField(attr="post_indexing"),
            "account": TextField(attr="account_indexing"),
            "comment": TextField(),
            "date": DateField(),
            "last_update": DateField(),
        }
    )

    class Django(object):
        """The model associate with this Document"""

        model = Post
