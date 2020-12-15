from django.urls import path
from .views import PostCommentListView, PostDetailView, PostImageView, PostListView


urlpatterns = [
    # url paths
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<uuid:unique_id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<uuid:unique_id>/comments/', PostCommentListView.as_view(), name='post-comments'),
    path('post/<uuid:unique_id>/image/', PostImageView.as_view(), name='blog-image'),
]