from books.views.views1 import (
    BookCommentListView,
    BookCommentDetailView,
    BookImageView,
    CartAddView,
    CartListView,
    CartDetailsView,
)
from books.views.views2 import (
    BookListView,
    BookDetailView,
    AuthorListView,
    AuthorDetailView,
    BooksByAuthorView,
    BooksByPublisherView,
    PublisherListView,
    PublisherDetailView,
)

from django.conf.urls import include
from django.urls import path

urlpatterns = [
    # url paths
    path("", BookListView.as_view(), name="book-list"),
    path("<uuid:unique_id>/", BookDetailView.as_view(), name="book-detail"),
    path("cart/items/", CartListView.as_view(), name="cart-items"),
    path(
        "cart/items/add/<uuid:unique_id>/", CartAddView.as_view(), name="cart-item-add"
    ),
    path("cart/items/<uuid:unique_id>/", CartDetailsView.as_view(), name="cart-item"),
    path("book/<uuid:unique_id>/images/", BookImageView.as_view(), name="book-image"),
    path("authors/", AuthorListView.as_view(), name="authors"),
    path("author/<uuid:unique_id>/", AuthorDetailView.as_view(), name="author-detail"),
    path(
        "author/<uuid:unique_id>/books/",
        BooksByAuthorView.as_view(),
        name="books-by-author",
    ),
    path(
        "book/comments/<uuid:unique_id>/",
        BookCommentDetailView.as_view(),
        name="book-comment",
    ),
    path(
        "book/<uuid:unique_id>/comments/",
        BookCommentListView.as_view(),
        name="book-comments",
    ),
    path("publishers/", PublisherListView.as_view(), name="publishers"),
    path(
        "publisher/<uuid:unique_id>/",
        PublisherDetailView.as_view(),
        name="publisher-detail",
    ),
    path(
        "publisher/<uuid:unique_id>/books/",
        BooksByPublisherView.as_view(),
        name="books-by-publisher",
    ),
]
