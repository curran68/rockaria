# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # placeholder
    path('', views.index, name='tickets_home'),
]
