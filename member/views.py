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

'''            Members of specific club Zone         '''
class ClubMemberView(APIView):
    serializer_class = MemberSerializer
    serializer_class = MemberProfileSerializer
    
    permission_classes = [AllowAny]

    def get_object(self, pk):  # Query a member of a given club id
        try:
            return CustomUser.objects.filter(memberProfile__club_id = pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get_objects(self, pk):  # Query the profile of a given member
        try:
            return MemberProfile.objects.filter(club_id = pk)
        except MemberProfile.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        serializer = {}
        member = self.get_object(self.kwargs.get('pk_club', ''))
        member = MemberSerializer(member, many = True).data

        memberprofile = self.get_objects(self.kwargs.get('pk_club', ''))
        memberprofile= MemberProfileSerializer(memberprofile, many = True).data
    
        #Dont touch this area hahahaha!
        new_dict = {}       # here convert one of list of dictionaries to dict
        for index in member:
           new_dict[index['id']]= index

        # here combine with the other list of dict
        combined = [dict(new_dict.get(d['user'], {}), **d) for d in memberprofile]    
        
        return Response(combined)
   


   
'''            Member Profile Zone         '''
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

    def get(self, request, format=None):
        profile = MemberProfile.objects.all()
        serializer = MemberProfileSerializer(profile, many=True)
        return Response(serializer.data)
   
#Retrieve, update or delete a program instance. 
class MemberProfileUpdateView(APIView):
    serializer_class = MemberProfileSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return MemberProfile.objects.get(pk=pk)
        except MemberProfile.DoesNotExist:
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
        profile = self.get_object(self.kwargs.get('pk_member', ''))
        serializer = MemberProfileSerializer(profile)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        '''            Members of All club Zone  | create member        '''
class MemberView(APIView):
    serializer_class = MemberProfileSerializer
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, format=None):
        member = CustomUser.objects.filter(roles = 6)
        member = MemberSerializer(member, many = True).data

        memberprofile = MemberProfile.objects.filter(user__roles = 6)
        memberprofile= MemberProfileSerializer(memberprofile, many = True).data

        #Dont touch this area hahahaha!
        new_dict = {}       # here convert one of list of dictionaries to dict
        for index in member:
           new_dict[index['id']]= index

        # here combine with the other list of dict
        combined = [dict(new_dict.get(d['user'], {}), **d) for d in memberprofile]    
        
        return Response(combined)
   
class MemberUpdateView(APIView):
    serializer_class = MemberSerializer
    serializer_class = MemberProfileSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):  # Query a member of a given Id
        try:
            return CustomUser.objects.filter(id = pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get_objects(self, pk):  # Query the profile of a given member
        try:
            return MemberProfile.objects.filter(user_id = pk)
        except MemberProfile.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        member = self.get_object(self.kwargs.get('pk_member', ''))
        member = MemberSerializer(member, many = True).data

        memberprofile = self.get_objects(self.kwargs.get('pk_member', ''))
        memberprofile= MemberProfileSerializer(memberprofile, many = True).data
    
        #Dont touch this area hahahaha!
        new_dict = {}       # here convert one of list of dictionaries to dict
        for index in member:
           new_dict[index['id']]= index

        # here combine with the other list of dict
        combined = [dict(new_dict.get(d['user'], {}), **d) for d in memberprofile]    
        
        return Response(combined)



