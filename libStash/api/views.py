from rest_framework import permissions, generics, status, viewsets, serializers
from rest_framework.response import Response
from djoser.views import UserViewSet
from djoser import signals, utils
from djoser.compat import get_user_email
from djoser.conf import settings
from books.models import *
from users.models import *
from .serializers import *
from django.http.response import Http404
from django.contrib.auth.tokens import default_token_generator


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
    serializer_class = BookDetailSerializer

class AuthorDetail(generics.RetrieveAPIView):


    """
    Get an author instance.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BooksByAuthor(generics.ListAPIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, *args, **kwargs):
        try:
            books = Book.objects.filter(author=self.get_object(kwargs['pk']))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404

class ImageDetail(generics.RetrieveAPIView):
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
    def retrieve(self, request, *args, **kwargs):
        images = Image.objects.filter(book=self.get_object(kwargs['pk']))
        serializer = ImageSerializer(images, many=True)
        return super().retrieve(request, *args, **kwargs)
    
class PublisherDetail(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BooksByPublisher(generics.ListAPIView):
    
    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, *args, **kwargs):
        try:
            books = Book.objects.filter(Publisher=self.get_object(kwargs['pk']))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404

class AddressList(generics.RetrieveAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def retrieve(self, request, *args, **kwargs):
        address = Address.objects.filter(account=request.user).order_by('-last_update')
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

class AddressCreate(generics.CreateAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['account'] = request.user
            serializer.save()
            return Response({'status': 'Address Created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


    def retrieve(self, request, *args, **kwargs):
        address = Address.objects.get(account=request.user, pk=kwargs['adrs_pk'])
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        address = Address.objects.get(account=request.user, pk=kwargs['adrs_pk'])
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Address Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        address = Address.objects.get(account=request.user, pk=kwargs['adrs_pk'])
        address.delete()
        return Response({'status': 'Address Deleted'})

class CartDetail(generics.RetrieveAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        cart = Cart.objects.get(account=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class BookInCartDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer

    def retrieve(self, request, *args, **kwargs):
        cart = Cart.objects.get(account=request.user)
        book_in_cart = BookInCart.objects.filter(cart=cart, pk=kwargs['pk'])
        serializer = BookInCartSerializer(book_in_cart, many=True)
        return Response(serializer.data)

class UserViewSet(UserViewSet):
    serializer_class = UserSerializer
    queryset = Account.objects.all()
    permission_classes = settings.PERMISSIONS.user
    token_generator = default_token_generator
    lookup_field = settings.USER_ID_FIELD

    def perform_create(self, serializer):
        
        user = serializer.save()
        cart = Cart.objects.create(account=user, is_active=True)
        cart.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {"user": user}
        to = [get_user_email(user)]
        if settings.SEND_ACTIVATION_EMAIL:
            settings.EMAIL.activation(self.request, context).send(to)
        elif settings.SEND_CONFIRMATION_EMAIL:
            settings.EMAIL.confirmation(self.request, context).send(to)

class AddToCart(generics.CreateAPIView):
    queryset = BookInCart.objects.all()
    serializer_class = AddToCartSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(account=request.user)
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['cart'] = cart
            serializer.save()
            return Response({'status': 'Added book to cart'})
        