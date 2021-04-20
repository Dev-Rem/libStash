from blogs.serializers import PostCommentSerializer, PostImageSerializer, PostSerializer
from blogs.models import Post, PostComment, PostImage

from permission import ReadOnly, IsOwner
from paginations import CustomPaginator

from decouple import config
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

# Create your views here.

CACHE_TTL = int(config("CACHE_TTL"))


class PostListView(ListAPIView):
    """GET: Returns all Post Instance"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPaginator
    permission_classes = [ReadOnly]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PostDetailView(RetrieveAPIView):
    """GET: Returns a Post instance"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ReadOnly]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class PostCommentView(ListCreateAPIView):
    """
    GET: Returns all Comments instance related to either a blog post or book review
    POST: Crete a book Comment object
    """

    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        post = Post.objects.get(unique_id=kwargs["unique_id"])
        comments = PostComment.objects.filter(post=post)
        serializer = PostCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        post = Post.objects.get(unique_id=kwargs["unique_id"])
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer._validated_data["post"] = post
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class PostCommentDetailView(RetrieveUpdateDestroyAPIView):
    """
    GET: retrieve  post comment instance
    UPDATE: Update  post comment instance
    DELETE: delete  post comment instance
    """

    serializer_class = PostCommentSerializer
    permission_classes = [IsOwner]
    lookup_field = "unique_id"

    def get_queryset(self):
        return PostComment.objects.get(unique_id=self.kwargs["unique_id"])

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        comment = self.get_queryset()
        serializer = PostCommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        comment = self.get_queryset()
        serializer = PostCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            comment = self.get_queryset()
            comment.delete()
            return Response({"status": "Success"})
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)


class PostImageView(RetrieveAPIView):
    """GET: Returns all images associated with the book instance."""

    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [ReadOnly]
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "unique_id"

    def get_queryset(self):
        post = Post.objects.filter(unique_id=self.kwargs["unique_id"])
        return PostImage.objects.filter(post=post)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = PostImageSerializer(
                queryset, many=True, context={"request": request}
            )
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)
