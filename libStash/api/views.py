from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from books.models import *
from users.models import *
from .serializers import *

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Author instances.
    POST: Create a new Author Instance
    PUT: Update an Author Instance
    PATCH: Partially update an Author instance
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

class BookViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Book instances.
    POST: Create a new Book Instance
    PUT: Update an Book Instance
    PATCH: Partially update an Book instance
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class ImageViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Image instances.
    POST: Create a new Image Instance
    PUT: Update an Image Instance
    PATCH: Partially update an Image instance
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]

class PublisherViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Publisher instances.
    POST: Create a new Publisher Instance
    PUT: Update an Publisher Instance
    PATCH: Partially update an Publisher instance
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminUser]

class WarehouseBookViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all WarehouseBook instances.
    POST: Create a new WarehouseBook Instance
    PUT: Update an WarehouseBook Instance
    PATCH: Partially update an WarehouseBook instance
    """
    queryset = WarehouseBook.objects.all()
    serializer_class = WarehouseBookSerializer
    permission_classes = [IsAdminUser]

class WarehouseViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Warehouse instances.
    POST: Create a new Warehouse Instance
    PUT: Update an Warehouse Instance
    PATCH: Partially update an Warehouse instance
    """
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAdminUser]

class AccountViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Account instances.
    POST: Create a new Account Instance
    PUT: Update an Account Instance
    PATCH: Partially update an Account instance
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]

class AddressViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Address instances.
    POST: Create a new Address Instance
    PUT: Update an Address Instance
    PATCH: Partially update an Address instance
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdminUser]

class BookInCartViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all BookInCart instances.
    POST: Create a new BookInCart Instance
    PUT: Update an BookInCart Instance
    PATCH: Partially update an BookInCart instance
    """
    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer
    permission_classes = [IsAdminUser]

class BookReviewViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all BookReview instances.
    POST: Create a new BookReview Instance
    PUT: Update an BookReview Instance
    PATCH: Partially update an BookReview instance
    """
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAdminUser] 

class CartViewSet(viewsets.ModelViewSet):
    """
    GET: Returns all Cart instances.
    POST: Create a new Cart Instance
    PUT: Update an Cart Instance
    PATCH: Partially update an Cart instance
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]









