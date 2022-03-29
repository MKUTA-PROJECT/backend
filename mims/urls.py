"""mims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from django.urls import path, include

...
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="MINMS API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Token and admin
    path('admin/', admin.site.urls),

    # Swagg Setting
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #Include account urls
    path('auth/', include('account.urls')),

    #Include Tb Info urls
    path('projects/', include('project.urls')),

    #Include clubs urls
    path('clubs/', include('club.urls')),

    #Include members urls
    path('members/', include('member.urls')),

    #Include staff urls
    path('staffs/', include('staff.urls')),

    #Include supervisor urls
    path('supervisor/', include('supervisor.urls')),

    #Include lookup urls
    path('lookup/', include('lookup.urls')),




    
]
