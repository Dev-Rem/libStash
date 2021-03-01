from django.urls import path
from .views import (
    PostCommentView,
    PostDetailView,
    PostImageView,
    PostListView,
)


urlpatterns = [
    # url paths
    path(
        "posts/",
        PostListView.as_view(),
        name="post-list",
    ),
    path(
        "post/<uuid:unique_id>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),
    path(
        "post/<uuid:unique_id>/comments/",
        PostCommentView.as_view(),
        name="post-comments",
    ),
<<<<<<< HEAD
    path(
        "post/<uuid:unique_id>/image/",
        PostImageView.as_view(),
        name="blog-image",
    ),
]
=======
    path("post/<uuid:unique_id>/image/", PostImageView.as_view(), name="blog-image"),
] 
>>>>>>> 6137b010210341b78fe2a774cbd84ea935e2fe7c
