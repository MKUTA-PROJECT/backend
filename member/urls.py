from django.urls import path
from django.conf.urls import url

from member.views import *

urlpatterns = [
    #Member
    path('', MemberProfileView.as_view(), name='Members'),
    path('<int:pk_member>/', MemberProfileUpdateView.as_view(), name='Update Member'),

    ]