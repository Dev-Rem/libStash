from books.serializers import (
    CartSerializer,
    BookInCartSerializer,
    BookCommentSerializer,
    BookImageSerializer,
)
from books.models import Cart, BookInCart, BookImage, BookComment, Book

from permission import IsOwner
from paginations import CustomPaginator

from decouple import config
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

CACHE_TTL = int(config("CACHE_TTL"))


class CartListView(ListAPIView):

    """
    GET: Returns all cart items
    POST: Add item to cart. Creates new BookInCart Instance.
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Cart.objects.get(account=self.request.user)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        try:
            cart = self.get_queryset()
            items = BookInCart.objects.filter(cart=cart)
            serializer = BookInCartSerializer(items, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)


class CartAddView(CreateAPIView):
    """POST: Add item to cart. Creates new BookInCart Instance."""

    queryset = BookInCart.objects.all()
    serializer_class = BookInCartSerializer
    permission_classes = [IsOwner]

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(account=self.request.user)
        book = Book.objects.get(unique_id=kwargs["unique_id"])
        serializer = BookInCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["cart"] = cart
            serializer.validated_data["book"] = book
            serializer.validated_data["quantity"] = request.data["quantity"]
            serializer.validated_data["amount"] = book.price
            serializer.save()
            return Response(status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CartDetailsView(RetrieveUpdateDestroyAPIView):
    """
    GET: Returns cart item
    PUT: Updates cart item
    DELETE: Deletes item from cart
    """

    serializer_class = CartSerializer
    permission_classes = [IsOwner]
    lookup_field = "unique_id"

    def get_queryset(self):
        return Cart.objects.get(account=self.request.user)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            cart = self.get_queryset()
            item = BookInCart.objects.get(cart=cart, unique_id=kwargs["unique_id"])
            serializer = BookInCartSerializer(item)
            return Response(serializer.data)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        cart = self.get_queryset()
        item = BookInCart.objects.get(cart=cart, unique_id=kwargs["unique_id"])
        serializer = BookInCartSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            cart = self.get_queryset()
            item = BookInCart.objects.get(cart=cart, unique_id=kwargs["unique_id"])
            item.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)


class BookCommentListView(ListCreateAPIView):
    """
    GET: Returns all Comments instance related to either a blog post or book review
    POST: Crete a book Comment object
    """

    queryset = BookComment.objects.all()
    serializer_class = BookCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        book = Book.objects.get(unique_id=kwargs["unique_id"])
        comments = BookComment.objects.filter(book=book)
        serializer = BookCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        book = Book.objects.get(unique_id=kwargs["unique_id"])
        serializer = BookCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer._validated_data["book"] = book
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class BookCommentDetailView(RetrieveUpdateDestroyAPIView):
    """
    GET: Returns user comment
    PATCH: Updates user comment
    DELETE: Deletes comment from post
    """

    serializer_class = BookCommentSerializer
    permission_classes = [IsOwner]
    lookup_field = "unique_id"

    def get_queryset(self):
        return BookComment.objects.get(unique_id=self.kwargs["unique_id"])

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            comment = self.get_queryset()
            serializer = BookCommentSerializer(comment)
            return Response(serializer.data)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        comment = self.get_queryset()
        serializer = BookCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.validated_data["comment"] = request.data["comment"]
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, requests, *args, **kwargs):
        try:
            comment = self.get_queryset()
            comment.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=HTTP_400_BAD_REQUEST)


class BookImageView(RetrieveAPIView):
    """GET: Returns all images associated with the book instance."""

    serializer_class = BookImageSerializer
    lookup_field = "unique_id"

    def get_queryset(self):
        book = Book.objects.get(unique_id=self.kwargs["unique_id"])
        return BookImage.objects.filter(book=book)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            image = self.get_queryset()
            serializer = BookImageSerializer(
                image, many=True, context={"request": request}
            )
            return Response(serializer.data)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)
