"""Required imports"""
from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from .models import Post, PostImage, PostComment

"""Get index name for setting"""
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])
INDEX.settings(number_of_shards=1, number_of_replicas=1)

"""HTML strip analyzer used by Elasticsearch to index document"""
html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


@INDEX.doc_type
class PostDocument(Document):
    """Post Elasticsearch document."""

    id = fields.IntegerField(attr="id")

    title = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    content = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
    )

    date = fields.DateField()

    last_update = fields.DateField()

    class Django(object):
        """Inner nested class Django."""

        model = Post  # The model associate with this Document
