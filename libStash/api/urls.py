from django.urls import path
from .views import (
    BookList,
    BookDetail,
    AuthorDetail,
    PublisherDetail,
    AccountViewSet,
    AddressDetail,
    CartDetail,
    BookInCartDetail,
)


account_create = AccountViewSet.as_view({"post": "create"})
account_detail = AccountViewSet.as_view({"get": "retrieve"})
account_edit = AccountViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update"}
)

urlpatterns = [
    # url paths
    path("", BookList.as_view()),
    path("book/<int:pk>/", BookDetail.as_view(), name="book-detail"),
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
    path("account/create/", account_create, name="account-create"),
    path("account/<int:pk>/", account_detail, name="account-detail"),
    path("account/<int:pk>/edit/", account_edit, name="account-edit"),
    path(
        "account/<int:pk>/address/",
        AddressDetail.as_view(),
        name="account-address",
    ),
    path(
        "account/<int:pk>/address/edit/",
        AddressDetail.as_view(),
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
