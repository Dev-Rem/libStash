from django.urls import path

from blogs.views import (
    PostCommentView,
    PostCommentDetailView,
    PostDetailView,
    PostImageView,
    PostListView,
)

urlpatterns = [
    # url paths
    path("", PostListView.as_view(), name="post-list"),
    path("<uuid:unique_id>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<uuid:unique_id>/image/", PostImageView.as_view(), name="post-image"),
    path(
        "post/<uuid:unique_id>/comments/",
        PostCommentView.as_view(),
        name="post-comments",
    ),
    path(
        "post/comments/<uuid:unique_id>/",
        PostCommentDetailView.as_view(),
        name="post_comment_detail",
    ),
]
