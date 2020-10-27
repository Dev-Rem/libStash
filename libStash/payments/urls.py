from django.urls import path
from django.conf.urls import url
from payments import views


urlpatterns = [
    # url paths

    path('checkout/sessions/', views.create_checkout_session, name='create-sessions'),
    # path('checkout/sessions/<int:id>'),
    # path('checkout/sessions/<int:id>'),
]
