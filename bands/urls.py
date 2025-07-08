# bands/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.band_list, name='band_list'),
    path('concerts/', views.concert_list, name='concert_list'),
    path('band/<slug:slug>/', views.band_detail, name='band_detail'),
]
