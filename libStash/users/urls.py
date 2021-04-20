from django.urls import path
from users.views import AddressCreateView, AddressUpdateView, UserViewSet

urlpatterns = [
    path("register/", UserViewSet.as_view({"post": "create"}), name="account-register"),
    path(
        "edit/<uuid:unique_id>/",
        UserViewSet.as_view({"patch": "partial_update"}),
        name="account-update",
    ),
    path("address/", AddressCreateView.as_view(), name="account-addresses"),
    path(
        "address/edit/<uuid:unique_id>/",
        AddressUpdateView.as_view(),
        name="account-address-edit",
    ),
    # auth/jwt/create/ POST: get refresh and access tokens
    # auth/jwt/refresh/ POST: get new access token
    # auth/users/me/  GET: get account info, POST: delete account
    # auth/users/me/set_password/ POST: account password reset
]
