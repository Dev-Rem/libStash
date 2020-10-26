from django.shortcuts import render
from books.models import Book
from api.serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics

# Create your views here.

class BookListView(generics.ListAPIView):
    """
    GET: Returns all book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Returns a book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    """
    GET: Returns an author instance.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BooksByAuthorView(generics.ListAPIView):
    """
    GET: Returns all books associated with an author Instance
    """

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, *args, **kwargs):
        try:
            books = Book.objects.filter(author=self.get_object(kwargs['pk']))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404

class ImageDetailView(generics.RetrieveAPIView):
    """
    GET: Returns all images associated with the book instance.
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # Get book instance
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Http404

    # Get images for book instance
    def retrieve(self, request, *args, **kwargs):
        images = Image.objects.filter(book=self.get_object(kwargs['pk']))
        serializer = ImageSerializer(images, many=True)
        return super().retrieve(request, *args, **kwargs)

class PublisherDetailView(generics.RetrieveAPIView):
    """
    GET: Returns a Publisher instance
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BooksByPublisherView(generics.ListAPIView):
    
    """
    GET: Returns all books associated with a publisher instance
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except:
            return Http404

    def retrieve(self, request, *args, **kwargs):
        try:
            books = Book.objects.filter(Publisher=self.get_object(kwargs['pk']))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            return Http404
            
class BookReviewListView(generics.ListCreateAPIView):
    """
    GET: Returns all book reviews
    POST: Crete a book review object
    """

    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Http404

    def list(self, request, *args, **kwargs):
        book = self.get_object(kwargs['pk'])
        reviews = BookReview.objects.filter(book=book)
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        book =self.get_object(kwargs['pk'])
        serializer = BookReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['account'] = request.user
            serializer._validated_data['book'] = book
            serializer.save()
            return super().create(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
