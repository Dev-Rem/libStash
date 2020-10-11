from django.urls import path, include
from .views import *

app_name = 'users'


urlpatterns = [
    # book related urls
    path("", BookList.as_view()),
    path("book/<int:pk>/", BookDetail.as_view(), name="book-detail"), # done
    path("author/<int:pk>/", AuthorDetail.as_view(), name="author-detail"), # done
    path('author/<int:pk>/books/', BooksByAuthor.as_view(), name='books-by-author'), # done
    path("publisher/<int:pk>/", PublisherDetail.as_view(), name="publisher-detail"), # done

    # account related urls
    path('account/register/', UserViewSet.as_view({'post': 'create'}), name='account-register'), # done
    path("account/address/create", AddressCreate.as_view(), name='addres-create'), # done
    path("account/address/", AddressList.as_view(), name="account-address"), # done
    path("account/address/edit/<int:adrs_pk>/", AddressUpdate.as_view(), name="account-address-edit"), # done
    path("account/address/delete/<int:adrs_pk>/", AddressUpdate.as_view(), name="account-address-delete"), # done
    path("account/cart/", CartDetail.as_view(),name="account-cart"), # done
    path('account/cart/book/edit/<int:pk>/',BookInCartDetail.as_view(), name='book-in-cart-edit'), # done
    path('account/cart/add-to-cart/',AddToCart.as_view(), name='add-to-cart'), # done

    # djoser urls for authentification
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),


]
