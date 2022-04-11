from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from club.models import Club
from member.models import Member, MemberProfile
from django.http import Http404
from rest_framework.response import Response

from project.models import Project
from staff.models import Staff

# Dashboard data

class DashboardView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # clubs, staffs, project, members counter

        try:
            clubs = Club.objects.all().count()
            members = Member.objects.all().count()
            projects = Project.objects.all().count()
            staffs = Staff.objects.all().count()

            
            #Members gender
            member_gender = {}
            member_gender['male'] = Member.objects.filter(sex=1).count() 
            member_gender['female'] = Member.objects.filter(sex=2).count()

            # Members who are post TB
            member_post_tb ={}
            member_post_tb['positive'] = MemberProfile.objects.filter(is_post_tb = True).count() 
            member_post_tb['negative'] = MemberProfile.objects.filter(is_post_tb = False).count() 

            return Response( {
                'clubs': clubs,
                'members':members,
                'projects': projects,
                'staffs': staffs,
                'gender':member_gender,
                'post_tb':member_post_tb
            },200)
        except:
            raise Http404
