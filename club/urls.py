from django.urls import path
from django.conf.urls import url
from club.views import *

urlpatterns = [
    #club 
    path('', ClubView.as_view(), name='clubs'),
    path('<int:pk_club>/', ClubUpdateView.as_view(), name='Update Club'),

    #members
    path('<int:pk_club>/member/', ClubMemberView.as_view(), name = 'members' ),

    # CSO
    path('cso/', CSOView.as_view(), name = 'cso' )    

    ]