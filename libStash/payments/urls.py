from django.urls import path
from django.conf.urls import url
from payments import views
urlpatterns = [
    # url paths

    url(r'^test-payment/$', views.test_payment),
]
