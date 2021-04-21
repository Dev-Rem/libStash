from django.urls import include, path
from rest_framework.routers import SimpleRouter

from searches.views import PostDocumentView, BookDocumentView

router = SimpleRouter()
posts = router.register("posts", PostDocumentView, basename="postdocument")
books = router.register("books", BookDocumentView, basename="bookdocument")

urlpatterns = router.urls
