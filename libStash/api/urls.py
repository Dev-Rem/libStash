from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    AccountViewSet, 
    AddressViewSet, 
    AuthorViewSet, 
    BookInCartViewSet, 
    BookViewSet, 
    CartViewSet, 
    CommentViewSet, 
    ImageViewSet, 
    PostViewSet, 
    PublisherViewSet, 
    WarehouseBookViewSet, 
    WarehouseViewSet,
) 
app_name = 'users'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='book-review')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'publishers', PublisherViewSet, basename='publisher')
router.register(r'warehousebooks', WarehouseBookViewSet, basename='warehousebook')
router.register(r'warehouses', WarehouseViewSet, basename='warehouse')
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'books-in-cart', BookInCartViewSet, basename='book-in-cart')
router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('book/', include('books.urls')),
    path('account/', include('users.urls')),
    path('admin/', include(router.urls) ),

]
