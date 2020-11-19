from api.serializers import AuthorSerializer, BookCommentSerializer, BookDetailSerializer, BookImageSerializer, BookInCartSerializer, BookSerializer, CartSerializer, PublisherSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import status, generics, permissions, viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from libStash import settings
from books.models import Author, Book, Publisher, BookComment, BookImage, Cart, BookInCart
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

class CartDetailView(generics.RetrieveAPIView):
    """
    GET: a cart instance associated with the logged in user.
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        cart = Cart.objects.get(account=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class BookInCartDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: All book instances in cart
    """
    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        cart = Cart.objects.get(account=request.user)
        book_in_cart = BookInCart.objects.get(cart=cart, pk=kwargs['unique_id'])
        serializer = BookInCartSerializer(book_in_cart, many=True)
        return Response(serializer.data)

class ManageItemView(viewsets.ViewSet):
    """
    POST: Add book to cart
    """
    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, request):
        try:
            return Cart.objects.get(account=request.user)
        except:
            return Http404

    def create(self, request):
        cart = self.get_object(request)
        serializer = BookInCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['cart'] = cart
            serializer.save()
            return Response({'status': ' Item added book to cart'})
    
    def destroy(self, request, *args, **kwargs):
        cart = self.get_object(request)
        item = BookInCart.object.get(cart=cart, unique_id=kwargs['uuid'])
        self.pre_delete(item)
        item.delete()
        self.post_delete(item)
        return Response({'status': ' Item removed from Cart'})


class BookCommentListView(generics.ListCreateAPIView):
    """
    GET: Returns all Comments instance related to either a blog post or book review
    POST: Crete a book Comment object
    """
    queryset = BookComment.objects.all()
    serializer_class = BookCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'unique_id'

    def get_object(self, unique_id):
        try:
            return Book.objects.get(unique_id=unique_id)
        except:
            return Http404

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        object_ = self.get_object(kwargs['unique_id'])
        comments = BookComment.objects.filter(book=object_)
        serializer = BookCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        object_ =self.get_object(kwargs['unique_id'])
        serializer = BookCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['account'] = request.user
            serializer._validated_data['book'] = object_
            serializer.save()
            return Response({'status': 'Comment posted'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookImageDetailView(generics.RetrieveAPIView):
    """
    GET: Returns all images associated with the book instance.
    """
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'unique_id'

    def get_object(self, unique_id):
        try:
            return Book.objects.get(unique_id=unique_id)
        except:
            raise Http404

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        object_ = self.get_object(kwargs['unique_id'])
        image = BookImage.objects.get(book=object_)
        serializer = BookImageSerializer(image)
        return Response(serializer.data)
