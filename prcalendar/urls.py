from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Calendar",
      default_version='v1',
      description="""
      ## Description
      Calendar which allows you to: 
      - add events
      - set up notifications
      - manage your subscriptions
      - get astrological predictions.""",
   ),
   public=True,
)

urlpatterns = [
    path('', include('events.urls')),
    path('', include('subscriptions.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
