from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from blog.models import Post,Comment,Image
from books.models import Author,Book,Warehouse,WarehouseBook,Publisher
from users.models import Account,Address,BookInCart,Cart
from .serializers import (
    PostSerializer,
    CommentSerializer,
    ImageSerializer,
    AuthorSerializer,
    BookSerializer,
    BookDetailSerializer,
    CommentSerializer,
    BookInCartSerializer,
    CartSerializer,
    PublisherSerializer,
    WarehouseBookSerializer,
    WarehouseSerializer,
    AccountSerializer,
    AddressSerializer,
)

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Post instances 
    POST: Create a new Post Instance
    PUT: Update an Post Instance
    PATCH: Partially update an Post instance
    DELETE: Delete an Post instance
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all BookReview instances.
    POST: Create a new BookReview Instance
    PUT: Update an BookReview Instance
    PATCH: Partially update an BookReview instance
    DELETE: Delete an BookReview instance
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class ImageViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Image instances.
    POST: Create a new Image Instance
    PUT: Update an Image Instance
    PATCH: Partially update an Image instance
    DELETE: Delete an Image instance
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AuthorViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Author instances 
    POST: Create a new Author Instance
    PUT: Update an Author Instance
    PATCH: Partially update an Author instance
    DELETE: Delete an Author instance
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class BookViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Book instances.
    POST: Create a new Book Instance
    PUT: Update an Book Instance
    PATCH: Partially update an Book instance
    DELETE: Delete an Book instance
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PublisherViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Publisher instances.
    POST: Create a new Publisher Instance
    PUT: Update an Publisher Instance
    PATCH: Partially update an Publisher instance
    DELETE: Delete an Publisher instance
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class WarehouseBookViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all WarehouseBook instances.
    POST: Create a new WarehouseBook Instance
    PUT: Update an WarehouseBook Instance
    PATCH: Partially update an WarehouseBook instance
    DELETE: Delete an WarehouseBook instance
    """
    queryset = WarehouseBook.objects.all()
    serializer_class = WarehouseBookSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class WarehouseViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Warehouse instances.
    POST: Create a new Warehouse Instance
    PUT: Update an Warehouse Instance
    PATCH: Partially update an Warehouse instance
    DELETE: Delete an Warehouse instance
    """
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AccountViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Account instances.
    POST: Create a new Account Instance
    PUT: Update an Account Instance
    PATCH: Partially update an Account instance
    DELETE: Delete an Account instance
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AddressViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Address instances.
    POST: Create a new Address Instance
    PUT: Update an Address Instance
    PATCH: Partially update an Address instance
    DELETE: Delete an Address instance
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class BookInCartViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all BookInCart instances.
    POST: Create a new BookInCart Instance
    PUT: Update an BookInCart Instance
    PATCH: Partially update an BookInCart instance
    DELETE: Delete an BookInCart instance
    """
    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class CartViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Cart instances.
    POST: Create a new Cart Instance
    PUT: Update an Cart Instance
    PATCH: Partially update an Cart instance
    DELETE: Delete an Cart instance
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
