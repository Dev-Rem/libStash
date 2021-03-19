from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostDocumentView

router = DefaultRouter()
posts = router.register(r"posts", PostDocumentView, basename="postdocument")

urlpatterns = [
    path("", include(router.urls)),
]
