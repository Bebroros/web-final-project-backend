from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('events.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('accounts/', include('allauth.urls')),
]
