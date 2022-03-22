from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from supervisor.serializer import *
from django.http import Http404
from rest_framework.response import Response
from supervisor.models import *
# Create your views here.

'''             Supervisor Zone       '''
# Retrieve all supervisors that are already registered and exist in the system

class SupervisorView(APIView):
    serializer_class = SupervisorSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        supervisor = Supervisor.objects.all()
        serializer = SupervisorSerializer(supervisor, many=True)
        return Response(serializer.data)


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


'''            Create, View, Update supervisor Profile        '''

class SupervisorProfileView(APIView):
    serializer_class = SupervisorProfileSerializer
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
            return SupervisorProfile.objects.get(user=pk)
        except SupervisorProfile.DoesNotExist:
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
        serializer = SupervisorProfileSerializer(supervisor)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        supervisor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
