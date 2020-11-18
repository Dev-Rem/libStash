from django.urls import path
from blog.views import CommentListView, ImageDetailView, PostDetailView, PostListView
from libStash import settings


urlpatterns = [
    # url paths
    path('', PostListView.as_view(), name='post-list'),
    path('post/<uuid:unique_id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<uuid:unique_id>/comments/', CommentListView.as_view(), name='post-comments'),
    path('post/<uuid:unique_id>/image/', ImageDetailView.as_view(), name='blog-image'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)