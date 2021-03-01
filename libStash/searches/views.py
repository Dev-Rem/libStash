"""Required imports"""
from django.shortcuts import render
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents import PostDocument
from .serializers import PostDocumentSerializer

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)

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
