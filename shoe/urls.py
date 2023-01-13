from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Shoe Store API",
      default_version='v1',
      description="An Api for Shoe orders",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shoe_admin@app.com"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls, name='django_admin'),
    path('orders/', include('orders.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('users_auth.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
