from blogs.models import Post, PostComment, PostImage
from books.models import (
    Author,
    Book,
    BookComment,
    BookImage,
    BookInCart,
    Cart,
    Publisher,
)
from dashboard.models import Warehouse, WarehouseBook
from users.models import Account, Address

from blogs.serializers import PostSerializer, PostImageSerializer, PostCommentSerializer
from dashboard.serializers import WarehouseBookSerializer, WarehouseSerializer


from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    """
    Admin Post model viewset
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

    def create(self, request, *args, **kwargs):
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
