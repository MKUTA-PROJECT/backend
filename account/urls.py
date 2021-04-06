from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url
from .views import UserLoginView

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserLoginView.as_view(), name='login'),
]