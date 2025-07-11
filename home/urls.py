from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('management/', views.product_management, name='product_management'),
    path('bands/', views.bands_view, name='bands'),        # This is for your 'Our Bands' button
    path('concerts/', views.concerts_view, name='concerts'),  # This is for your 'Concerts' button
    path('book-tickets/', views.book_tickets_view, name='book_tickets'),
    path('privacy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms/', views.terms_view, name='terms_of_service'),
    path('contact/', views.contact_view, name='contact'),
    path('basket/', views.view_basket_view, name='view_basket'),
    path('book-tickets/<int:concert_id>/', views.book_tickets_for_concert, name='book_tickets_for_concert'),
    path('booking/success/', views.booking_success, name='booking_success'),

  # Also ensure this one is there for the basket button
]