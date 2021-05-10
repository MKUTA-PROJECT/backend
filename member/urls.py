from django.urls import path
from django.conf.urls import url

from member.views import *

urlpatterns = [
    #Member
    path('', MemberView.as_view(), name='Members'),
    path('<int:pk_member>/', MemberUpdateView.as_view(), name='Update Member'),

    #Member Profile
    path('profile/', MemberProfileView.as_view(), name='Members'),
    path('profile/<int:pk_member>/', MemberProfileUpdateView.as_view(), name='Update Member'),

    ]