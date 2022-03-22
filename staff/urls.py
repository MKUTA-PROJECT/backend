from django.urls import path
from django.conf.urls import url

from staff.views import *

urlpatterns = [
    #Staff
    path('', StaffView.as_view(), name='staffs'),
    path('<int:pk_staff>/', StaffUpdateView.as_view(), name='Update staff'),
    #staff Profile
    path('<int:pk_staff>/profile/', StaffProfileView.as_view(), name='staffs profile'),


    ]