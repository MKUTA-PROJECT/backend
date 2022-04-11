from django.urls import path
from django.conf.urls import url
from lookup.views import *

urlpatterns = [
    #Member Roles
    path('memberroles/', MemberRoleLookupView.as_view(), name='member roles'),
    path('memberroles/<str:pk_memberrole>/', MemberRoleLookupUpdateView.as_view(), name='member roles updtate'),
    
    #Member Roles
    path('staffroles/', StaffRoleLookupView.as_view(), name='staff roles'),
    path('staffroles/<str:pk_staffrole>/', StaffRoleLookupUpdateView.as_view(), name='staff roles updtate'),
    
    #Location
    path('location/', LocationLookupView.as_view(), name='Location'),
    path('location/<str:pk_location>/', LocationLookupUpdateView.as_view(), name='Location updtate'),
]

