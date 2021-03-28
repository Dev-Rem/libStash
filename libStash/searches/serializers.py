"""Required imports"""
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from .documents import PostDocument


class PostDocumentSerializer(DocumentSerializer):
    """
    Serializer for the BookDocument.
    """

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = PostDocument
        fields = ["id", "title", "content", "date", "last_update"]
