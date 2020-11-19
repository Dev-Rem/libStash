from django.urls import path
from users.views import AddressListView, AddressUpdateView, UserViewSet 

urlpatterns = [
    
    path('register/', UserViewSet.as_view({'post': 'create'}), name='account-register'), # done
    path("address/", AddressListView.as_view(), name="account-address"), # done
    path("address/edit/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-edit"), # done
    path("address/delete/<uuid:unique_id>/", AddressUpdateView.as_view(), name="account-address-delete"), # done
   ]
