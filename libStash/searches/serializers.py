"""Required imports"""
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from blogs.models import Post, PostImage, PostComment

from searches.documents.post import PostDocument
from searches.documents.postimage import PostImageDocument
from searches.documents.postcomment import PostCommentDocument


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
