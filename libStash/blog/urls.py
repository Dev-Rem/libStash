from django.urls import path
from blog.views import PostCommentListView, PostDetailView, PostImageDetailView, PostListView


urlpatterns = [
    # url paths
    path('', PostListView.as_view(), name='post-list'),
    path('post/<uuid:unique_id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<uuid:unique_id>/comments/', PostCommentListView.as_view(), name='post-comments'),
    path('post/<uuid:unique_id>/image/', PostImageDetailView.as_view(), name='blog-image'),
]