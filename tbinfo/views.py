from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from tbinfo.serializer import *
from django.http import Http404
from rest_framework.response import Response
from tbinfo.models import *

# Create your views here.
'''            Info Zone         '''
class TbInfoView(APIView):
    serializer_class = TbInfoSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, format=None):
        info = TbInfo.objects.all()
        serializer = TbInfoSerializer(info, many=True)
        return Response(serializer.data)
   
#Retrieve, update or delete a program instance. 
class TbInfoUpdateView(APIView):
    serializer_class = TbInfoSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return TbInfo.objects.get(pk=pk)
        except TbInfo.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        info_key = self.get_object(self.kwargs.get('pk_info', ''))
        serializer = self.serializer_class(info_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        info = self.get_object(self.kwargs.get('pk_info', ''))
        serializer = TbInfoSerializer(info)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        info = self.get_object(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)