from django.urls import path
from .views import BookList, BookDetail, AuthorDetail

urlpatterns = [
    # url paths
    path("", BookList.as_view()),
    path("book/<int:pk>", BookDetail.as_view(), name="book_detail"),
    path("author/<int:pk>", AuthorDetail.as_view(), name="author_deatail"),
]
