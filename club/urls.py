from django.urls import path
from django.conf.urls import url
from club.views import *
from member.views import ClubMemberView

urlpatterns = [
    #club 
    path('', ClubView.as_view(), name='clubs'),
    path('<int:pk_club>/', ClubUpdateView.as_view(), name='Update Club'),
    path('<int:pk_club>/supervisor/', ClubSupervisorView.as_view(), name='Update Club'),

    #supervisors
    path('supervisor/', SupervisorView.as_view(), name='supervisors'), # all or create
    path('supervisor/<int:pk_supervisor>/', SupervisorUpdateView.as_view(), name='Update supervisor'),

    #members
    path('<int:pk_club>/member/', ClubMemberView.as_view(), name = 'members' )
    

]