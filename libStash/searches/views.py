"""Required imports"""
from django_elasticsearch_dsl_drf.constants import (LOOKUP_FILTER_RANGE,
                                                    LOOKUP_QUERY_GT,
                                                    LOOKUP_QUERY_GTE,
                                                    LOOKUP_QUERY_IN,
                                                    LOOKUP_QUERY_LT,
                                                    LOOKUP_QUERY_LTE)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend, FilteringFilterBackend, IdsFilterBackend,
    OrderingFilterBackend, SearchFilterBackend)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet

from .documents import PostDocument
from .serializers import PostDocumentSerializer

# Create your views here.


class PostDocumentView(BaseDocumentViewSet):
    """
    The Post Document view.
    """

    document = PostDocument
    serializer_class = PostDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define the search fields
    search_fields = [
        "title",
        "content",
    ]

    # Define filter fields
    filter_fields = {
        "id": {
            "field": "id",
            "lookups": [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        "title": "title.raw",
        "content": "content.raw",
        "date": "date",
        "last_update": "last_update",
    }

    # Define Ordering fields
    ordering_fields = {
        "id": "id",
        "title": "title.raw",
        "content": "content.raw",
        "date": "date",
        "last_update": "last_update",
    }

    ordering = ["id", "title"]
