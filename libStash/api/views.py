from books.models import Publisher, Book, Author, Warehouse, WarehouseBook, Image
from .serializers import (
    PublisherSerializer,
    AuthorSerializer,
    BookSerializer,
    ImageSerializer,
    # WarehouseSerializer,
    # WarehouseBookSerilizer
)
from rest_framework import generics

# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ImageDetail(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PublisherDetail(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer