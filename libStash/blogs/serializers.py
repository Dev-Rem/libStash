from blogs.models import Post, PostComment, PostImage
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class PostSerializer(ModelSerializer):
    """
    Serializer for the Post model.
    """

    account = SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = Post
        fields = [
            "unique_id",
            "title",
            "content",
            "account",
            "likes",
            "date",
        ]


class PostImageSerializer(ModelSerializer):
    """Serializer for the PostImage model."""

    post = SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = PostImage
        fields = ["unique_id", "post", "image"]


class PostCommentSerializer(ModelSerializer):
    """Serializer for the PostComment model."""

    account = SlugRelatedField(slug_field="unique_id", read_only=True)
    post = SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = PostComment
        fields = ["unique_id", "post", "account", "comment", "date"]
