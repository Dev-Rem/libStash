from django.urls import path
from books.views import *


# urlpatterns = [
#     # url paths
#     path("books/", BookListView.as_view()),
#     path("book/<uuid:unique_id>/", BookDetailView.as_view(), name="book-detail"), # done
#     path('book/<uuid:unique_id>/reviews/', BookReviewListView.as_view(), name='book-reviews'),
#     path("author/<uuid:unique_id>/", AuthorDetailView.as_view(), name="author-detail"), # done
#     path('author/<uuid:unique_id>/books/', BooksByAuthorView.as_view(), name='books-by-author'), # done
#     path("publisher/<uuid:unique_id>/", PublisherDetailView.as_view(), name="publisher-detail"), # done
# ]
