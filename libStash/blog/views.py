from django.shortcuts import render
from .models import Post, Comment, Image
from api.serializers import CommentSerializer, ImageSerializer, PostSerializer
from rest_framework import permissions, status, generics
from books.models import Book
from django.http import Http404
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from libStash import settings
from django.db.models import ObjectDoesNotExist
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL')


class PostListView(generics.ListAPIView):
    """
    GET: Returns all Post Instance
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'unique_id'

    # @method_decorator(vary_on_cookie)
    # @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class PostDetailView(generics.RetrieveAPIView):
    '''
    GET: Returns a Post instance
    '''

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class CommentListView(generics.ListCreateAPIView):
    """
    GET: Returns all Comments instance related to either a blog post or book review
    POST: Crete a book Comment object
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'unique_id'

    def get_object(self, unique_id):
        try:
            return Post.objects.get(unique_id=unique_id)
        except ObjectDoesNotExist:
            return Book.objects.get(unique_id=unique_id)
        except:
            return Http404

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        object_ = self.get_object(kwargs['unique_id'])
        try:
            comments = Comment.objects.filter(post=object_)
        except:
            comments = Comment.objects.filter(book=object_)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        object_ =self.get_object(kwargs['unique_id'])
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['account'] = request.user
            if isinstance(object_, Post):
                serializer._validated_data['post'] = object_
                # serializer.save()
            else:
                serializer._validated_data['book'] = object_
            serializer.save()
            return Response({'status': 'Comment posted'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDetailView(generics.RetrieveAPIView):
    """
    GET: Returns all images associated with the book instance.
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'unique_id'

    def get_object(self, unique_id):
        try:
            return Post.objects.get(unique_id=unique_id)
        except ObjectDoesNotExist:
            return Book.objects.get(unique_id=unique_id)
        except:
            return Http404

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        object_ = self.get_object(kwargs['unique_id'])
        try:
            image = Image.objects.get(post=object_)
        except:
            image = Image.objects.get(book=object_)
        serializer = ImageSerializer(image)
        return Response(serializer.data)
