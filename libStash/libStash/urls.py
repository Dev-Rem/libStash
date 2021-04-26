"""libStash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from libStash.settings import base as settings

urlpatterns = [
    # DJANGO DEFAULT ADMIN
    path(settings.ADMIN_URL, admin.site.urls),
    # USER ACCOUNT MANAGEMENT
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# API URLS
urlpatterns += [
    path('api/v1/dashboard/', include('dashboard.urls')),
    path("api/v1/blogs/", include("blogs.urls")),
    path("api/v1/books/", include("books.urls")),
    path("api/v1/payments/", include("payments.urls")),
    path("api/v1/searches/", include("searches.urls")),
    path("api/v1/users/", include("users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
