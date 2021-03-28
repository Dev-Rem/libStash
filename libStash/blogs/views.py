from api.serializers import (PostCommentSerializer, PostImageSerializer,
                             PostSerializer)
from blogs.models import Post, PostComment, PostImage
from decouple import config
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics, permissions, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

# Create your views here.

CACHE_TTL = int(config("CACHE_TTL"))


class PostListView(generics.ListAPIView):
    """
    GET: Returns all Post Instance
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PostDetailView(generics.RetrieveAPIView):
    """
    GET: Returns a Post instance
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class PostCommentView(generics.ListCreateAPIView):
    """
    GET: Returns all Comments instance related to either a blog post or book review
    POST: Crete a book Comment object
    """

    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "unique_id"

    def get_object(self, unique_id):
        try:
            return Post.objects.get(unique_id=unique_id)
        except ObjectDoesNotExist:
            return Http404

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        post = self.get_object(kwargs["unique_id"])
        comments = PostComment.objects.filter(post=post)
        serializer = PostCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        post = self.get_object(kwargs["unique_id"])
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer._validated_data["post"] = post
            serializer.save()
            return redirect(request.path_info)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostImageView(generics.RetrieveAPIView):
    """
    GET: Returns all images associated with the book instance.
    """

    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "unique_id"

    def get_object(self, unique_id):
        try:
            return Post.objects.get(unique_id=unique_id)
        except ObjectDoesNotExist:
            raise Http404

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            post = self.get_object(kwargs["unique_id"])
            image = PostImage.objects.filter(post=post)
            serializer = PostImageSerializer(
                image, many=True, context={"request": request}
            )
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise Http404
