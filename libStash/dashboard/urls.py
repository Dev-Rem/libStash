from dashboard.views.views1 import (
    PublisherViewSet,
    AuthorViewSet,
    BookViewSet,
    BookImageViewSet,
    BookCommentViewSet,
    AccountViewSet,
    AddressViewSet,
    BookInCartViewSet,
    CartViewSet,
)
from dashboard.views.views2 import (
    PostViewSet,
    PostImageViewSet,
    PostCommentViewSet,
    WarehouseBookViewSet,
    WarehouseViewSet,
)

from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"post-comments", PostCommentViewSet, basename="post-comments")
router.register(r"post-images", PostImageViewSet, basename="post-images")
router.register(r"publishers", PublisherViewSet, basename="publisher")
router.register(r"authors", AuthorViewSet, basename="author")
router.register(r"books", BookViewSet, basename="book")
router.register(r"book-comments", BookCommentViewSet, basename="book-comments")
router.register(r"book-images", BookImageViewSet, basename="book-images")
router.register(r"carts", CartViewSet, basename="carts")
router.register(r"books-in-cart", BookInCartViewSet, basename="book-in-cart")
router.register(r"warehousebooks", WarehouseBookViewSet, basename="warehousebook")
router.register(r"warehouses", WarehouseViewSet, basename="warehouse")
router.register(r"accounts", AccountViewSet, basename="account")
router.register(r"addresses", AddressViewSet, basename="address")

urlpatterns = [
    path("dashboard/", include(router.urls)),
]
