from elasticsearch_dsl.connections import connections
from .models import Post

connections.create_connection(hosts=["localhost"])

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


@registry.register_document
class PostDocument(PostDocument):
    title = fields.CharField(attr="title")
    content = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(),
        },
    )

    class Index:
        name = "Post_data"

    class Django:
        model = Post
