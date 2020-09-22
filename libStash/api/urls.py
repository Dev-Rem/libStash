from django.urls import path
from .views import (
    BookList,
    BookDetail,
    AuthorDetail,
    PublisherDetail,
    AccountDetail,
    AddessDetail,
    CartDetail,
    BookInCartDetail,
)

urlpatterns = [
    # url paths
    path("", BookList.as_view()),
    path(
        "book/<int:pk>/",
        BookDetail.as_view(),
        name="book-detail",
    ),
    path(
        "author/<int:pk>/",
        AuthorDetail.as_view(),
        name="author-detail",
    ),
    path(
        "publisher/<int:pk>/",
        PublisherDetail.as_view(),
        name="publisher-detail",
    ),
    path(
        "account/<int:pk>/",
        AccountDetail.as_view(),
        name="account-detail",
    ),
    path(
        "account/<int:pk>/edit/",
        AccountDetail.as_view(),
        name="account-edit",
    ),
    path(
        "account/<int:pk>/address/",
        AddessDetail.as_view(),
        name="account-address",
    ),
    path(
        "account/<int:pk>/address/edit/",
        AddessDetail.as_view(),
        name="account-address-edit",
    ),
    path(
        "account/<int:pk>/cart/",
        CartDetail.as_view(),
        name="account-cart",
    ),
    path(
        "account/<int:pk>/cart-book/",
        BookInCartDetail.as_view(),
        name="account-cart-book",
    ),
]
