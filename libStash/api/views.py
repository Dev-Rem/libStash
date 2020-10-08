from rest_framework import permissions, generics, status, viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import *
from users.models import *
from .serializers import *
from django.http.response import Http404

from django.shortcuts import redirect


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

class AuthorDetail(generics.RetrieveAPIView):


    """
    Get an author instance.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BooksByAuthor(viewsets.ViewSet):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, pk=None):
        try:
            books = Book.objects.filter(author=self.get_object(pk))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404

class ImageDetail(generics.RetrieveAPIView):
    """
    Get all image instances associated with the book instance.
    """

    # # Get book instance
    # def get_object(self, pk):
    #     try:
    #         return Book.objects.get(pk=pk)
    #     except:
    #         return Http404

    # # Get images for book instance

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def get(self, request, pk, format=None):
        images = Image.objects.filter(book=self.get_object(pk))
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class PublisherDetail(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BooksByPublisher(viewsets.ViewSet):
    
    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, pk=None):
        try:
            books = Book.objects.filter(Publisher=self.get_object(pk))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404

class AddressList(generics.RetrieveAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_account(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, *args, **kwargs):
        account = self.get_account(pk=kwargs['pk'])
        address = Address.objects.filter(account=account).order_by('-last_update')
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

class AddressCreate(generics.CreateAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        account = Account.objects.get(email=request.user)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['account'] = account
            serializer.save()
            return Response({'status': 'Address Created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_account(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, *args, **kwargs):
        account = self.get_account(kwargs['pk'])
        address = Address.objects.get(account=account, pk=kwargs['adrs_pk'])
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        account = self.get_account(kwargs['pk'])
        address = Address.objects.get(account=account, pk=kwargs['adrs_pk'])
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Address Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        account = self.get_account(kwargs['pk'])
        address = Address.objects.get(account=account, pk=kwargs['adrs_pk'])
        address.delete()
        return Response({'status': 'Address Deleted'})

class CartDetail(APIView):

    def get(self, request, format=None):

        cart = Cart.objects.get(account=request.user)
        context = {
            'request': request
        }
        serializer = CartSerializer(cart, context=context)
        return Response(serializer.data)

class BookInCartDetail(generics.RetrieveAPIView):

    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer

    def retrieve(self, request, *args, **kwargs):
        cart = Cart.objects.get(account=request.user)
        book_in_cart = BookInCart.objects.filter(cart=cart, pk=kwargs['pk'])
        serializer = BookInCartSerializer(book_in_cart, many=True)
        return super().retrieve(request, *args, **kwargs)


# class AddToCart(generics.CreateAPIView):
    
#     def create(self, request, *args, **kwargs):
#         cart = Cart.objects.get(account=request.user)
#         book = Book.objects.get(pk=kwargs['pk'])
#         serializer = BookInCartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.validated_data['cart'] = cart
#             serializer.validated_data['book'] = book
#             return Response({'status': 'Added book to cart'})
        