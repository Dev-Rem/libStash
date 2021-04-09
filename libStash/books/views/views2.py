from books.serializers import AuthorSerializer, BookSerializer, PublisherSerializer
from books.models import Author, Book, Publisher

from permission import IsOwner
from paginations import CustomPaginator

from decouple import config
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

CACHE_TTL = int(config("CACHE_TTL"))

# Create your views here.


class BookListView(ListAPIView):
    """
    GET: Returns all book instance.
    """

    queryset = Book.objects.all().order_by("last_update")
    serializer_class = BookSerializer
    pagination_class = CustomPaginator
    filter_backends = [SearchFilter]
    search_fields = ["title", "format", "year"]

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BookDetailView(RetrieveAPIView):
    """
    GET: Returns a book instance.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "unique_id"

    def get_queryset(self):
        return Book.objects.get(unique_id=self.kwargs["unique_id"])

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            book = self.get_queryset()
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)


class AuthorListView(ListAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class AuthorDetailView(RetrieveAPIView):
    """GET: Returns an author instance."""

    serializer_class = AuthorSerializer
    lookup_field = "unique_id"

    def get_queryset(self):
        return Author.objects.get(unique_id=self.kwargs["unique_id"])

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            author = self.get_queryset()
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)


class BooksByAuthorView(ListAPIView):
    """GET: Returns all books associated with an author Instance"""

    serializer_class = BookSerializer
    pagination_class = CustomPaginator
    lookup_field = "unique_id"

    def get_queryset(self):
        author = Author.objects.get(unique_id=self.kwargs["unique_id"])
        books = Book.objects.filter(author=author)
        return books

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        try:
            books = self.get_queryset()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class PublisherListView(ListAPIView):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class PublisherDetailView(RetrieveAPIView):
    """GET: Returns a Publisher instance"""

    serializer_class = PublisherSerializer
    lookup_field = "unique_id"

    def get_queryset(self):
        return Publisher.objects.get(unique_id=self.kwargs["unique_id"])

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            publisher = self.get_queryset()
            serializer = PublisherSerializer(publisher)
            return Response(serializer.data)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)


class BooksByPublisherView(ListAPIView):
    """GET: Returns all books associated with a publisher instance"""

    serializer_class = BookSerializer
    lookup_field = "unique_id"

    def get_queryset(self):
        publisher = Publisher.objects.get(unique_id=self.kwargs["unique_id"])
        books = Book.objects.filter(publisher=publisher)
        return books

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        try:
            books = self.get_queryset()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Response(status=HTTP_404_NOT_FOUND)
