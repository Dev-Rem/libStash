from api.views import (AccountViewSet, AddressViewSet, AuthorViewSet,
                       BookCommentViewSet, BookImageViewSet, BookInCartViewSet,
                       BookViewSet, CartViewSet, PostCommentViewSet,
                       PostImageViewSet, PostViewSet, PublisherViewSet,
                       WarehouseBookViewSet, WarehouseViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "users"

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"book-comments", BookCommentViewSet, basename="book-comments")
router.register(r"post-comments", PostCommentViewSet, basename="post-comments")
router.register(r"book-images", BookImageViewSet, basename="book-images")
router.register(r"post-images", PostImageViewSet, basename="post-images")
router.register(r"authors", AuthorViewSet, basename="author")
router.register(r"books", BookViewSet, basename="book")
router.register(r"publishers", PublisherViewSet, basename="publisher")
router.register(r"warehousebooks", WarehouseBookViewSet, basename="warehousebook")
router.register(r"warehouses", WarehouseViewSet, basename="warehouse")
router.register(r"accounts", AccountViewSet, basename="account")
router.register(r"address", AddressViewSet, basename="address")
router.register(r"books-in-cart", BookInCartViewSet, basename="book-in-cart")
router.register(r"carts", CartViewSet, basename="cart")

urlpatterns = [
    path("blogs/", include("blogs.urls")),
    path("books/", include("books.urls")),
    path("account/", include("users.urls")),
    path("dashboard/", include(router.urls)),
]
