from django.urls import path
from django.conf.urls import url

from activity.views import *

urlpatterns = [
    #Info
    path('', ActivityView.as_view(), name='activity'),
    path('<int:pk_activity>/', ActivityUpdateView.as_view(), name='Update Activity'),
    ]