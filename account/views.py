
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect

from account.serializers import UserLoginSerializer

from account.models import CustomUser


# Create your views here.
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'email': serializer.data['email'],
                'role': serializer.data['role'],
                'name' : serializer.data['name'], 
                'id': serializer.data['id']        
            }

            return Response(response, status=status_code)
       