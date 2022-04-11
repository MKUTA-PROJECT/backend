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

class MemberRoleLookupUpdateView(APIView):
    serializer_class = MemberRoleLookupSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return MemberRoleLookup.objects.get(pk=pk)
        except MemberRoleLookup.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        memberrole = self.get_object(self.kwargs.get('pk_memberrole', ''))
        serializer = MemberRoleLookupSerializer(memberrole)

        return Response(serializer.data)

'''            StaffRole Zone         '''
class StaffRoleLookupView(APIView):
    serializer_class = StaffRoleLookupSerializer
    permission_classes = [AllowAny]
 

    def get(self, request, format=None):
        club = StaffRoleLookup.objects.all()
        serializer = StaffRoleLookupSerializer(club, many=True)
        return Response(serializer.data)

class StaffRoleLookupUpdateView(APIView):
    serializer_class = StaffRoleLookupSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return StaffRoleLookup.objects.get(pk=pk)
        except StaffRoleLookup.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        staffrole = self.get_object(self.kwargs.get('pk_staffrole', ''))
        serializer = StaffRoleLookupSerializer(staffrole)

        return Response(serializer.data)


'''            Location Zone         '''
class LocationLookupView(APIView):
    serializer_class = LocationLookupSerializer
    permission_classes = [AllowAny]
 

    def get(self, request, format=None):
        club = LocationLookup.objects.all()
        serializer = LocationLookupSerializer(club, many=True)
        return Response(serializer.data)

class LocationLookupUpdateView(APIView):
    serializer_class = LocationLookupSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return LocationLookup.objects.get(healthfacilitylookup__club=pk)
        except LocationLookup.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        location_key = self.get_object(self.kwargs.get('pk_location', ''))
        serializer = self.serializer_class(location_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        location = self.get_object(self.kwargs.get('pk_location', ''))
        serializer = LocationLookupSerializer(location)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)