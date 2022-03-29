from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from member.serializer import *
from django.http import Http404
from rest_framework.response import Response
from member.models import *
from account.models import CustomUser

# Create your views here.


'''            Create, View, Update Staff Profile        '''
class MemberProfileView(APIView):
    serializer_class = MemberProfileSerializer
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
            return MemberProfile.objects.get(user=pk)
        except MemberProfile.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        agency_key = self.get_object(self.kwargs.get('pk_member', ''))
        serializer = self.serializer_class(agency_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        agency = self.get_object(self.kwargs.get('pk_member', ''))
        serializer = MemberProfileSerializer(agency)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        agency = self.get_object(pk)
        agency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''            Members of All Members      '''
class MemberView(APIView):
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        member = Member.objects.all()
        member = MemberSerializer(member, many=True).data
        return Response(member, 200)

'''            Update specific member     '''
class MemberUpdateView(APIView):
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):  # Query a member of a given Id
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        member_key = self.get_object(self.kwargs.get('pk_member', ''))
        serializer = self.serializer_class(member_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        member = self.get_object(self.kwargs.get('pk_member', ''))
        member = MemberSerializer(member).data

        return Response(member)
