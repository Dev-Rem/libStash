from django.urls import path
from books.views import *


urlpatterns = [
    # url paths
    path("books", BookListView.as_view()),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"), # done
    path('book/<int:pk>/reviews/', BookReviewListView.as_view(), name='book-reviews'),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"), # done
    path('author/<int:pk>/books/', BooksByAuthorView.as_view(), name='books-by-author'), # done
    path("publisher/<int:pk>/", PublisherDetailView.as_view(), name="publisher-detail"), # done
]
