from django.urls import path
from django.conf.urls import url

from project.views import *
urlpatterns = [
    # Project
    path('', ProjectView.as_view(), name='project'),
    path('<int:pk_project>/', ProjectUpdateView.as_view(), name='Update project'),

    # members
    path('<int:pk_project>/member/',
         ProjectMemberView.as_view(), name='Project members')
]
