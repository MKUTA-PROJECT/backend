from django.urls import path
from django.conf.urls import url

from supervisor.views import *

urlpatterns = [
    #supervisor
    path('', SupervisorView.as_view(), name='supervisors'),
    path('<int:pk_supervisor>/', SupervisorUpdateView.as_view(), name='Update supervisor'),
    #supervisor Profile
    path('<int:pk_supervisor>/profile/', SupervisorProfileView.as_view(), name='supervisors profile'),


    ]