# rockaria/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from home.views import custom_logout_view

urlpatterns = [
    # Custom logout view must go BEFORE allauth
    path('accounts/logout/', custom_logout_view, name='account_logout'),

    # Alias 'login' to allauth's login view for admin compatibility
    path('login/', RedirectView.as_view(pattern_name='account_login'), name='login'),

    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('bands/', include('bands.urls')),
    path('tickets/', include('tickets.urls')),
    path('payments/', include('payments.urls')),
    path('admin/', admin.site.urls),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)