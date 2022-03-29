from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from lookup.serializer import *
from lookup.models import *


# Create your views here.

'''            MemberRole Zone         '''
class MemberRoleLookupView(APIView):
    serializer_class = MemberRoleLookupSerializer
    permission_classes = [AllowAny]
 

    def get(self, request, format=None):
        club = MemberRoleLookup.objects.all()
        serializer = MemberRoleLookupSerializer(club, many=True)
        return Response(serializer.data)