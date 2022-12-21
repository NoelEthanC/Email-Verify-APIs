from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from .swagger import BothHttpAndHttpsSchemaGenerator
import json

schema_view = get_schema_view(
   openapi.Info(
      title="Email-Verify API",
      default_version='v1',
      description="An API that will allow users to send sign up and the API will verify there emails by sending the emails usung the email submitted on sign up  ",
      # generator_class= type(json.dumps(BothHttpAndHttpsSchemaGenerator.get_schema())),
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="noelchiwamba1@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
      generator_class= BothHttpAndHttpsSchemaGenerator,
   # url='https://email-verify-api.up.railway.app/',
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', include('accounts.urls'))
]
