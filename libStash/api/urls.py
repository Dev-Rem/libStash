from django.urls import path, include
from .views import *

app_name = 'users'

books_by_author = BooksByAuthor.as_view({'get': 'retrieve'})

urlpatterns = [
    # url paths
    path("", BookList.as_view()),
    path("book/<int:pk>/", BookDetail.as_view(), name="book-detail"), # done
    # path('<int:pk>/add-to-cart/',AddToCart.as_view(), name='add-to-cart'),
    path("author/<int:pk>/", AuthorDetail.as_view(), name="author-detail"), # done
    path('author/<int:pk>/books/', books_by_author, name='books-by-author'), # done
    path("publisher/<int:pk>/", PublisherDetail.as_view(), name="publisher-detail"), # done
    path("account/<int:pk>/address/create", AddressCreate.as_view(), name='addres-create'), # done
    path("account/<int:pk>/address/", AddressList.as_view(), name="account-address"), # done
    path("account/<int:pk>/address/<int:adrs_pk>/edit/", AddressUpdate.as_view(), name="account-address-edit"), # done
    path("account/<int:pk>/address/<int:adrs_pk>/delete/", AddressUpdate.as_view(), name="account-address-delete"), 
    path("account/cart/", CartDetail.as_view(),name="account-cart"), # done
    path('account/cart/<int:pk>/book-in-cart/',BookInCartDetail.as_view(), name='book-in-cart'),
    path("cart-book/<int:pk>", BookInCartDetail.as_view(), name="book-in-cart"),
    path('cart-book/<int:pk>/edit', BookInCartDetail.as_view(), name='book-in-cart-edit'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
