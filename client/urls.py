from django.urls import path
from django.conf.urls import url
from client.views import *


urlpatterns = [
    #club 
    path('', ClientView.as_view(), name='clients'),
    path('<int:pk_client>/', ClientUpdateView.as_view(), name='Update Client'),

]