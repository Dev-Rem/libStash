"""Required imports"""
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from blogs.models import Post, PostImage, PostComment

from searches.documents.posts.post import PostDocument
from searches.documents.posts.postimage import PostImageDocument
from searches.documents.posts.postcomment import PostCommentDocument
from searches.documents.books.book import BookDocument
from searches.documents.books.bookimage import BookImageDocument
from searches.documents.books.bookcomment import BookCommentDocument
from searches.documents.books.author import AuthorDocument
from searches.documents.books.publisher import PublisherDocument


class PostImageDocumentSerializer(DocumentSerializer):
    """Serializer for the PostImageDocument."""

    class Meta:
        document = PostImageDocument
        exclude = ["id"]


class PostCommentDocumentSerializer(DocumentSerializer):
    """Serializer for the PostCommentDocument."""

    class Meta:
        document = PostCommentDocument
        exclude = ["id"]


class PostDocumentSerializer(DocumentSerializer):
    """Serializer for the PostDocument."""

    postImage = PostImageDocumentSerializer(many=True)
    postComment = PostCommentDocumentSerializer(many=True)

    class Meta:
        document = PostDocument
        fields = [
            "id",
            "unique_id",
            "title",
            "content",
            "date",
            "is_active",
            "last_update",
            "postImage",
            "postComment",
        ]


class AuthorDocumentSerializer(DocumentSerializer):
    """Serializer for the AuthorDocument."""

    class Meta:
        document = AuthorDocument
        exclude = ["id"]


class PublisherDocumentSerializer(DocumentSerializer):
    """Serializer for the PublisherDocument."""

    class Meta:
        document = PublisherDocument
        exclude = ["id"]


class BookImageDocumentSerializer(DocumentSerializer):
    """Serializer for the BookImageDocument."""

    class Meta:
        document = BookImageDocument
        exclude = ["id"]


class BookCommentDocumentSerializer(DocumentSerializer):
    """Serializer for the BookCommnetDocument."""

    class Meta:
        document = BookCommentDocument
        exclude = ["id"]


class BookDocumentSerializer(DocumentSerializer):
    """Serializer for the BookDocument."""

    author = AuthorDocumentSerializer(many=True)
    publisher = PublisherDocumentSerializer()
    bookImage = BookImageDocumentSerializer(many=True)
    bookComment = BookCommentDocumentSerializer(many=True)

    class Meta:
        document = BookDocument
        fields = [
            "id",
            "unique_id",
            "title",
            "isbn",
            "year",
            "price",
            "last_update",
            "author",
            "publisher",
            "bookImage",
            "bookComment",
        ]
