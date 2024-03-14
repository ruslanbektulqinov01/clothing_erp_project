
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="http://127.0.0.1:8000/api/swagger",
      default_version='v1',
      description="clothing erp project API",
      terms_of_service="",
      contact=openapi.Contact(email="ruslanbek.tulqinov.01@bk.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,]
)

urlpatterns = [
   path('api/admin/', admin.site.urls),
   path('api/', include('clothing.routers')),
   path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

