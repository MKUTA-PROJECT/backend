from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from staff.serializer import *
from django.http import Http404
from rest_framework.response import Response
from staff.models import *
from account.models import CustomUser


'''             Staff Zone       '''
# Retrieve all supervisors that are already registered and exist in the system

class StaffView(APIView):
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        agency = Staff.objects.all()
        serializer = StaffSerializer(agency, many=True)
        return Response(serializer.data)


class StaffUpdateView(APIView):
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        agency_key = self.get_object(self.kwargs.get('pk_staff', ''))
        serializer = self.serializer_class(agency_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        agency = self.get_object(self.kwargs.get('pk_staff', ''))
        serializer = StaffSerializer(agency)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        agency = self.get_object(pk)
        agency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''            Create, View, Update Staff Profile        '''

class StaffProfileView(APIView):
    serializer_class = StaffProfileSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get_object(self, pk):
        try:
            return StaffProfile.objects.get(user=pk)
        except StaffProfile.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        agency_key = self.get_object(self.kwargs.get('pk_staff', ''))
        serializer = self.serializer_class(agency_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        agency = self.get_object(self.kwargs.get('pk_staff', ''))
        serializer = StaffProfileSerializer(agency)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        agency = self.get_object(pk)
        agency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
