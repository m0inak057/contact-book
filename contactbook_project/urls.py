from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add allauth URLs
    path('accounts/', include('allauth.urls')),
    # Your app URLs
    path('', include('contacts.urls')),
]
