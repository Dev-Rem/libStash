from api.serializers import BookDetailSerializer,BookSerializer,AuthorSerializer,PublisherSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import status, generics, permissions
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from libStash import settings
from books.models import Author, Book, Publisher
CACHE_TTL = getattr(settings, 'CACHE_TTL')

# Create your views here.

class BookListView(generics.ListAPIView):
    """
    GET: Returns all book instance.
    """
    queryset = Book.objects.all().order_by('last_update')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author', 'category', 'publisher', 'format', 'year', 'price']
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Returns a book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class AuthorDetailView(generics.RetrieveAPIView):
    """
    GET: Returns an author instance.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["name",]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class BooksByAuthorView(generics.ListAPIView):
    """
    GET: Returns all books associated with an author Instance
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'unique_id'

    def get_object(self, unique_id):
        try:
            return Author.objects.get(unique_id=unique_id)
        except:
            return Http404
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            books = Book.objects.filter(author=self.get_object(kwargs['unique_id']))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404

class PublisherDetailView(generics.RetrieveAPIView):
    """
    GET: Returns a Publisher instance
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["name",]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class BooksByPublisherView(generics.ListAPIView):
    
    """
    GET: Returns all books associated with a publisher instance
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'unique_id'

    def get_object(self, unique_id):
        try:
            return Publisher.objects.get(unique_id=unique_id)
        except:
            return Http404

    def retrieve(self, request, *args, **kwargs):
        try:
            books = Book.objects.filter(Publisher=self.get_object(kwargs['unique_id']))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404
            