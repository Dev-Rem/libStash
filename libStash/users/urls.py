from django.urls import path
from users.views import ManageItemView, AddressListView, AddressUpdateView, BookInCartDetailView, CartDetailView, UserViewSet 

urlpatterns = [
    
    path('register/', UserViewSet.as_view({'post': 'create'}), name='account-register'), # done
    path("address/", AddressListView.as_view(), name="account-address"), # done
    path("address/edit/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-edit"), # done
    path("address/delete/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-delete"), # done
    path("cart/", CartDetailView.as_view(),name="account-cart"), # done
    path('cart/book/edit/<uuid:unique_id>/',BookInCartDetailView.as_view(), name='book-in-cart-edit'), # done
    path('cart/add-to-cart/',ManageItemView.as_view({'post': 'create'}), name='add-to-cart'), # done
    path('cart/remove-from-cart/<uuid:unique_id>/',ManageItemView.as_view({'delete': 'destroy'}), name='remove-from-cart'), # done
]
