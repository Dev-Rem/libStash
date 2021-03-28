from blogs.models import Post, PostComment, PostImage
from books.models import (Author, Book, BookComment, BookImage, BookInCart,
                          Cart, Publisher, Warehouse, WarehouseBook)
from decouple import config
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from users.models import Account, Address

from .serializers import (AccountSerializer, AddressSerializer,
                          AuthorSerializer, BookCommentSerializer,
                          BookImageSerializer, BookInCartSerializer,
                          BookSerializer, CartSerializer,
                          PostCommentSerializer, PostImageSerializer,
                          PostSerializer, PublisherSerializer,
                          WarehouseBookSerializer, WarehouseSerializer)

CACHE_TTL = int(config("CACHE_TTL"))

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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Post created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostImageViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all PostImage instances.
    POST: Create a new PostImage instance
    PUT: Update an PostImage instance
    PATCH: Partially update an PostImage instance
    DELETE: Delete an PostImage instance
    """

    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = PostImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Post image created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCommentViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all PostComment instances.
    POST: Create a new PostComment Instance
    PUT: Update an PostComment Instance
    PATCH: Partially update an PostComment instance
    DELETE: Delete an PostComment instance
    """

    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Post comment created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Publisher created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Author created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Book created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookImageViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all BookImage instances.
    POST: Create a new BookImage instance
    PUT: Update an BookImage instance
    PATCH: Partially update an BookImage instance
    DELETE: Delete an BookImage instance
    """

    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = BookImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Book image created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookCommentViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all BookComment instances.
    POST: Create a new BookComment Instance
    PUT: Update an BookComment Instance
    PATCH: Partially update an BookComment instance
    DELETE: Delete an BookComment instance
    """

    queryset = BookComment.objects.all()
    serializer_class = BookCommentSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = BookCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Book comment created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = WarehouseBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Post created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
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
    search_fields = "__all__"
    ordering_fields = "__all__"
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
