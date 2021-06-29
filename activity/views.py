from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from activity.serializer import *
from django.http import Http404
from rest_framework.response import Response
from activity.models import *

# Create your views here.
'''            activity Zone         '''
class ActivityView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, format=None):
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)
   
#Retrieve, update or delete a program instance. 
class ActivityUpdateView(APIView):
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        activity_key = self.get_object(self.kwargs.get('pk_activity', ''))
        serializer = self.serializer_class(activity_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        activity = self.get_object(self.kwargs.get('pk_activity', ''))
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)