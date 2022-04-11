from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from club.serializer import *
from django.http import Http404
from rest_framework.response import Response
from club.models import *
from lookup.serializer import LocationLookupSerializer
from member.models import Member
from member.serializer import MemberSerializer

'''            Club Zone         '''
class ClubView(APIView):
    serializer_class = ClubSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, format=None):
        club = Club.objects.all().order_by('name')
        serializer = ClubSerializer(club, many=True)
        return Response(serializer.data)
   
#Retrieve, update or delete a program instance. 
class ClubUpdateView(APIView):
    serializer_class = ClubSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Club.objects.get(pk=pk)
        except Club.DoesNotExist:
            raise Http404
    def get_objects(self, pk):
        try:
            # healthfacility = HealthFacilityLookup.objects.get(club=pk)
            return LocationLookup.objects.get(healthfacilitylookup__club=pk)
        except LocationLookup.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        club_key = self.get_object(self.kwargs.get('pk_club', ''))
        serializer = self.serializer_class(club_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        club = self.get_object(self.kwargs.get('pk_club', ''))
        club = ClubSerializer(club).data

        # Location
        location = self.get_objects(self.kwargs.get('pk_club', ''))
        location = LocationLookupSerializer(location).data
        
        club_location = {}
        club_location.update(club)
        club_location.update(location)
        return Response(club_location)

    def delete(self, request, pk, format=None):
        club = self.get_object(pk)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''            Members of specific club Zone         '''
class ClubMemberView(APIView):
    serializer_class = MemberSerializer  
    permission_classes = [AllowAny]

    def get_object(self, pk):  # Query a member of a given club id
        try:
            return Member.objects.filter(memberProfile__club_id = pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        member = self.get_object(self.kwargs.get('pk_club', ''))
        member = MemberSerializer(member, many = True).data        
        return Response(member,200)


'''            CSO Zone         '''
class CSOView(APIView):
    serializer_class = MemberSerializer  
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        cso = CSO.objects.all()
        serializer = CSOSerializer(cso, many=True)
        return Response(serializer.data)

    