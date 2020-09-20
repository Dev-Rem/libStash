from django.urls import path
from .views import BookList, BookDetail, AuthorDetail

urlpatterns = [
    # url paths
    path("books/", BookList.as_view()),
    path("books/<int:pk>", BookDetail.as_view()),
    path("authors/<int:pk>", AuthorDetail.as_view()),
]
