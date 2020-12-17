from django.urls import path
from users.views import AddressListView, AddressUpdateView, UserViewSet 

urlpatterns = [
    
    path('register/', UserViewSet.as_view({'post': 'create'}), name='account-register'), # done
    path('edit/<uuid:unique_id>/', UserViewSet.as_view({'patch': 'partial_update'}), name='account-update'),
    path("address/", AddressListView.as_view(), name="account-addresses"), # done
    path("address/<uuid:unique_id>/", AddressListView.as_view(), name="account-address"), # done
    path("address/edit/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-edit"), # done
    path("address/delete/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-delete"), # done
    # auth/token/login/ login token url
    # auth/users/me/  account info, delete, update url
    # auth/users/me/set_password/ account password reset url

   ]
