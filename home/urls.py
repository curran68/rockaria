from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('management/', views.product_management, name='product_management'),
    path('admin/', admin.site.urls),  # This is for the Django admin interface
    path('bands/', views.bands_view, name='bands'),        # This is for your 'Our Bands' button
    path('concerts/', views.concerts_view, name='concerts'),  # This is for your 'Concerts' button
    path('book-tickets/', views.book_tickets_view, name='book_tickets'),
    path('basket/', views.view_basket_view, name='view_basket'), # Also ensure this one is there for the basket button
]