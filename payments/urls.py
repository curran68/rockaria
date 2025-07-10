# payments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # A page to initiate the checkout (e.g., a product detail page, or a simple "buy now" page)
    # This view would render an HTML page with a button that calls create_checkout_session
    path('buy/', views.buy_product_view, name='buy_product'),

    # Endpoint to create the Stripe Checkout Session (called via JavaScript)
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),

    # Stripe Webhook endpoint (Stripe sends events here)
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),

    # Success and Cancel URLs for Stripe Checkout redirects
    path('success/', views.payment_success_view, name='payment_success'),
    path('cancel/', views.payment_cancel_view, name='payment_cancel'),
]