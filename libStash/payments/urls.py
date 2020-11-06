from django.urls import path
from django.conf.urls import url
from payments import views


urlpatterns = [
    # url paths

    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('config/', views.stripe_config, name='config'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('checkout/success/', views.SuccessView.as_view(), name='checkout-success'),
    path('checkout/cancel/', views.CancelView.as_view(), name='checkout-cancel'),
    path('webhook/', views.stripe_webhook, name='stripe=webhook'),
]
