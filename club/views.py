from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from club.serializer import *
from django.http import Http404
from rest_framework.response import Response
from club.models import *

'''            Supevisor Zone         '''
class SupervisorView(APIView):
    serializer_class = SupervisorSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)
    def get(self, request, format=None):
        supervisor = Supervisor.objects.all()
        serializer = SupervisorSerializer(supervisor, many=True)
        return Response(serializer.data)
   
#Retrieve, update or delete a program instance. 
class SupervisorUpdateView(APIView):
    serializer_class = SupervisorSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Supervisor.objects.get(pk=pk)
        except Supervisor.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        supervisor_key = self.get_object(self.kwargs.get('pk_supervisor', ''))
        serializer = self.serializer_class(supervisor_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        supervisor = self.get_object(self.kwargs.get('pk_supervisor', ''))
        serializer = SupervisorSerializer(supervisor)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        supervisor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''            ClubSupervisor Zone           '''
class ClubSupervisorView(APIView):
    serializer_class = ClubSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Supervisor.objects.filter(club__id = pk)
        except Supervisor.DoesNotExist:
            raise Http404

   
    def get(self, request,*args, **kwargs):
        supervisor = self.get_object(self.kwargs.get('pk_club', ''))
        serializer = SupervisorSerializer(supervisor, many=True)
        return Response(serializer.data)

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
        club = Club.objects.all()
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
        serializer = ClubSerializer(club)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        club = self.get_object(pk)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
