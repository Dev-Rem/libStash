from rest_framework import permissions, generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import IsRegistered
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


class BookList(generics.ListAPIView):
    """
    List all books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    """
    Get a book instance.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


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

    # Get images for book instance
    def get(self, request, pk, format=None):
        images = Image.objects.filter(book=self.get_object(pk))
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)


class PublisherDetail(APIView):
    """
    Get a publisher instance.
    """

    def get(self, request, pk, format=None):
        publisher = Publisher.objects.get(pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AddressDetail(APIView):
    """
    Get, Create, Update, Edit an address instance.
    """

    # Get account instance
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except:
            return Http404

    # Use account instance to get account address
    def get(self, request, pk, format=None):
        address = Address.objects.get(account=self.get_object(pk))
        serializer = AddressSerializer(Address)
        return Response(serializer.data)

    # Use account instance to create account address
    def post(self, request, pk, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Use account instance to update account address
    def put(self, request, pk, format=None):
        address = Address.objects.get(account=self.get_object(pk))
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Use account instance to delete account address
    def delete(self, request, pk, format=None):
        address = Address.objects.get(account=self.get_object(pk))
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartDetail(APIView):
    """
    Get, Create, Update, Edit an address instance.
    """

    # Get account instance
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except:
            return Http404

    # Get an instance of account cart
    def get(self, request, pk, format=None):
        cart = Cart.objects.get(account=self.get_object(pk))
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class BookInCartDetail(APIView):
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None):
        book = Book.objects.filter(cart=self.get_object(pk))
        serializer = BookInCartSerializer(book, many=True)
        return Response(serializer.data)
