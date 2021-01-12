from django.urls import path
from books.views import AuthorDetailView, BookCommentListView, BookDetailView, BookImageView, BookListView, BooksByAuthorView, BooksByPublisherView, CartDetailView, ManageCartView, PublisherDetailView 
from rest_framework.routers import DefaultRouter
from django.conf.urls import include




urlpatterns = [
    # url paths
    
    path("", BookListView.as_view(), name='book-list'), 
    path("<uuid:unique_id>/", BookDetailView.as_view(), name="book-detail"), 
    path('<uuid:unique_id>/comments/', BookCommentListView.as_view(), name='book-comments'),
    path('<uuid:unique_id>/image/', BookImageView.as_view(), name='book-image'),
    path("author/<uuid:unique_id>/", AuthorDetailView.as_view(), name="author-detail"),
    path('author/<uuid:unique_id>/books/', BooksByAuthorView.as_view(), name='books-by-author'), 
    path("publisher/<uuid:unique_id>/", PublisherDetailView.as_view(), name="publisher-detail"),
    path('publisher/<uuid:unique_id>/books/', BooksByPublisherView.as_view(), name='books-by-publisher'), 
    path('cart/', CartDetailView.as_view(), name='cart=items'), 
    path('cart/item/<uuid:unique_id>/', ManageCartView.as_view({'get': 'retrieve'}), name='item'), 
    path('cart/add/item/<uuid:unique_id>/', ManageCartView.as_view({'post': 'create'}), name='add-item'), 
    path('cart/remove/item/<uuid:unique_id>/', ManageCartView.as_view({'delete': 'destroy'}), name='remove-item'), 
    path('cart/edit/item/<uuid:unique_id>/', ManageCartView.as_view({'put': 'update'}), name='edit-item'), 
]
