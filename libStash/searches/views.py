"""Required imports"""
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet

from paginations import CustomPaginator

from searches.documents.posts.post import PostDocument
from searches.documents.books.book import BookDocument
from searches.serializers import PostDocumentSerializer, BookDocumentSerializer


# Create your views here.

NUMBERLOOKUPS = [
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
]
STRINGLOOKUPS = [
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_EXCLUDE,
]


class PostDocumentView(BaseDocumentViewSet):
    """PostDocument viewset"""

    document = PostDocument
    serializer_class = PostDocumentSerializer
    pagination_class = CustomPaginator
    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
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
            "lookups": NUMBERLOOKUPS,
        },
        "title": {
            "field": "title",
            "lookups": STRINGLOOKUPS,
        },
        "content": {
            "field": "content",
            "lookups": STRINGLOOKUPS,
        },
        "date": "date",
        "is_active": "is_active",
        "last_update": "last_update",
    }

    # Define Ordering fields
    ordering_fields = {
        "id": "id",
        "date": "date",
        "last_update": "last_update",
    }

    ordering = ["id", "date"]


class BookDocumentView(BaseDocumentViewSet):
    """BookDocument viewset"""

    document = BookDocument
    serializer_class = BookDocumentSerializer
    pagination_class = CustomPaginator
    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]

    # Define the search fields
    search_fields = [
        "title",
        "year",
        "price",
        "author",
        "publisher",
    ]

    # Define filter fields
    filter_fields = {
        "id": {
            "field": "id",
            "lookups": NUMBERLOOKUPS,
        },
        "title": {
            "field": "title",
            "lookups": STRINGLOOKUPS,
        },
        "year": {
            "field": "content",
            "lookups": NUMBERLOOKUPS,
        },
        "date": "date",
        "last_update": "last_update",
    }

    # Define Ordering fields
    ordering_fields = {
        "id": "id",
        "date": "date",
        "last_update": "last_update",
    }

    ordering = ["id"]
