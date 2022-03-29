from django.urls import path
from django.conf.urls import url
from lookup.views import *

urlpatterns = [
    #Member Roles
    path('memberroles/', MemberRoleLookupView.as_view(), name='member roles'),


]