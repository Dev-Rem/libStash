from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostDocumentView

router = SimpleRouter()
posts = router.register("search", PostDocumentView, basename="postdocument")

urlpatterns = router.urls
