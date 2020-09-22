from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import Publisher, Book, Author, Warehouse, WarehouseBook, Image
from users.models import Account, Address, Cart, BookInCart
from .serializers import (
    PublisherSerializer,
    AuthorSerializer,
    BookSerializer,
    ImageSerializer,
    AccountSerializer,
    AddressSerializer,
    CartSerializer,
    BookInCartSerializer,
)
from django.http.response import Http404


# Create your views here.


class BookList(APIView):
    """
    List all books.
    """

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetail(APIView):
    """
    Get a book instance.
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AuthorDetail(APIView):
    """
    Get an author instance.
    """

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    #   Get other books the author have written
    def get_similar_books(self, pk):
        try:
            books = Book.objects.filter(author=self.get_object(pk))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404


class ImageDetail(APIView):
    """
    Get all image instances associated with the book instance.
    """

    # Get book instance
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Http404

    def get(self, pk, request, format=None):
        images = Image.objects.filter(book=self.get_object(pk))
        serili


class PublisherDetail(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AccountDetail(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AddessDetail(generics.RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CartDetail(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class BookInCartDetail(generics.RetrieveUpdateAPIView):
    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer