from django.urls import path
from django.conf.urls import url
from dashboard.views import *

urlpatterns = [
    #Member Roles
    path('', DashboardView.as_view(), name='member roles'),

]

