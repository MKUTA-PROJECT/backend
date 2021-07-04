from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from client.serializer import *
from django.http import Http404
from rest_framework.response import Response
from client.models import *

# Create your views here.
'''            Client Zone         '''
class ClientView(APIView):
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, format=None):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)
   
#Retrieve, update or delete a program instance. 
class ClientUpdateView(APIView):
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        Client_key = self.get_object(self.kwargs.get('pk_client', ''))
        serializer = self.serializer_class(Client_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        Client = self.get_object(self.kwargs.get('pk_client', ''))
        serializer = ClientSerializer(Client)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        Client = self.get_object(pk)
        Client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientFilterView(APIView):
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk, pk2):
        try:
            return Client.objects.all().filter(date__range=(pk, pk2))
        except Client.DoesNotExist:
            raise Http404  

    def get(self, request, *args, **kwargs):
        info = self.get_object(self.kwargs.get('pk_start', ''), self.kwargs.get('pk_end', ''))
        serializer = ClientSerializer(info, many=True)
        return Response(serializer.data)