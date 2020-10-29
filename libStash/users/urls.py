from django.urls import path, include
from djoser.views import UserViewSet
from users.views import *


# urlpatterns = [
#     # url paths
#     path('account/register/', UserViewSet.as_view({'post': 'create'}), name='account-register'), # done
#     path("account/address/", AddressListView.as_view(), name="account-address"), # done
#     path("account/address/edit/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-edit"), # done
#     path("account/address/delete/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-delete"), # done
#     path("account/cart/", CartDetailView.as_view(),name="account-cart"), # done
#     path('account/cart/book/edit/<uuid:unique_id>/',BookInCartDetailView.as_view(), name='book-in-cart-edit'), # done
#     path('account/cart/add-to-cart/',AddToCartView.as_view(), name='add-to-cart'), # done

# ]
