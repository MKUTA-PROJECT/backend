from django.urls import path
from django.conf.urls import url

from tbinfo.views import *

urlpatterns = [
    #Info
    path('', TbInfoView.as_view(), name='Info'),
    path('<int:pk_info>/', TbInfoUpdateView.as_view(), name='Update Info'),
    ]