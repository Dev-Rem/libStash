from django.urls import path
from books.views import AuthorDetailView, BookDetailView, BookListView, BooksByAuthorView, BooksByPublisherView, PublisherDetailView 
from blog.views import CommentListView, ImageDetailView


urlpatterns = [
    # url paths
    path("", BookListView.as_view(), name='book-list'),
    path("<uuid:unique_id>/", BookDetailView.as_view(), name="book-detail"), # done
    path('<uuid:unique_id>/comments/', CommentListView.as_view(), name='book-comments'),
    path('<uuid:unique_id>/image/', ImageDetailView.as_view(), name='book-image'),
    path("author/<uuid:uunique_idid>/", AuthorDetailView.as_view(), name="author-detail"), # done
    path('author/<uuid:unique_id>/books/', BooksByAuthorView.as_view(), name='books-by-author'), # done
    path("publisher/<uuid:unique_id>/", PublisherDetailView.as_view(), name="publisher-detail"), # done
    path('publisher/<uuid:unique_id>/books', BooksByPublisherView.as_view(), name='books-by-publisher'),
]
