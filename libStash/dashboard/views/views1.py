from books.models import (
    Publisher,
    Author,
    Book,
    BookImage,
    BookComment,
    BookInCart,
    Cart,
)
from users.models import Account, Address
from books.serializers import (
    PublisherSerializer,
    AuthorSerializer,
    BookSerializer,
    BookImageSerializer,
    BookCommentSerializer,
    BookInCartSerializer,
    CartSerializer,
)
from users.serializers import AccountSerializer, AddressSerializer

from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


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
