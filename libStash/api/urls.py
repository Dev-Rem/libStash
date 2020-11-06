from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import *
from books.views import *
from api.views import *

app_name = 'users'

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'publishers', PublisherViewSet, basename='publisher')
router.register(r'warehousebooks', WarehouseBookViewSet, basename='warehousebook')
router.register(r'warehouses', WarehouseViewSet, basename='warehouse')
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'books-in-cart', BookInCartViewSet, basename='book-in-cart')
router.register(r'book-reviews', BookReviewViewSet, basename='book-review')
router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [

    path("books/", BookListView.as_view(), name='book-list'),
    path("book/<uuid:unique_id>/", BookDetailView.as_view(), name="book-detail"), # done
    path('book/<uuid:unique_id>/cover/', ImageDetailView.as_view(), name='book-cover'),
    path('book/<uuid:unique_id>/reviews/', BookReviewListView.as_view(), name='book-reviews'),
    path("author/<uuid:uunique_idid>/", AuthorDetailView.as_view(), name="author-detail"), # done
    path('author/<uuid:unique_id>/books/', BooksByAuthorView.as_view(), name='books-by-author'), # done
    path("publisher/<uuid:unique_id>/", PublisherDetailView.as_view(), name="publisher-detail"), # done
    path('publisher/<uuid:unique_id>/books', BooksByPublisherView.as_view(), name='books-by-publisher'),
    path('account/register/', UserViewSet.as_view({'post': 'create'}), name='account-register'), # done
    path("account/address/", AddressListView.as_view(), name="account-address"), # done
    path("account/address/edit/<uuid:unique_id/", AddressUpdateView.as_view(), name="account-address-edit"), # done
    path("account/address/delete/<uuid:unique_id", AddressUpdateView.as_view(), name="account-address-delete"), # done
    path("account/cart/", CartDetailView.as_view(),name="account-cart"), # done
    path('account/cart/book/edit/<uuid:unique_id>/',BookInCartDetailView.as_view(), name='book-in-cart-edit'), # done
    path('account/cart/add-to-cart/',AddToCartView.as_view(), name='add-to-cart'), # done
    
    # admin related urls
    path('admin/', include(router.urls) ),

]
