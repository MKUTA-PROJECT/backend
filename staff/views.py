from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from staff.serializer import *
from django.http import Http404
from rest_framework.response import Response
from staff.models import *
from account.models import CustomUser


'''            All staffs  | create staff        '''

class StaffView(APIView):
    serializer_class = StaffProfileSerializer
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, format=None):
       staff = CustomUser.objects.filter(roles = 2)
       staff =StaffSerializer(staff, many = True).data

       staffprofile =StaffProfile.objects.filter(user__roles = 2)
       staffprofile=StaffProfileSerializer(staffprofile, many = True).data

        #Dont touch this area hahahaha!
       new_dict = {}       # here convert one of list of dictionaries to dict
       for index in staff:
            new_dict[index['id']]= index

        # here combine with the other list of dict
       combined = [dict(new_dict.get(d['user'], {}), **d) for d in staffprofile]    
        
       return Response(combined)
   
class StaffUpdateView(APIView):
    serializer_class =StaffProfileSerializer
    serializer_class =StaffSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):  # Query a staff of a given Id
        try:
            return CustomUser.objects.filter(id = pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get_objects(self, pk):  # Query the profile of a given staff
        try:
            return StaffProfile.objects.filter(user_id = pk)
        except StaffProfile.DoesNotExist:
            raise Http404
        # I had to add this in order to allow the put to operate, it query by Id
    def get_object_put(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        staff_key = self.get_object_put(self.kwargs.get('pk_stnaff', ''))
        serializer = self.serializer_class(staff_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
       staff = self.get_object(self.kwargs.get('pk_staff', ''))
       staff =StaffSerializer(staff, many = True).data

       staffprofile = self.get_objects(self.kwargs.get('pk_staff', ''))
       staffprofile=StaffProfileSerializer(staffprofile, many = True).data
    
        #Dont touch this area hahahaha!
       new_dict = {}       # here convert one of list of dictionaries to dict
       for index in staff:
            new_dict[index['id']]= index

    # here combine with the other list of dict
       combined = [dict(new_dict.get(d['user'], {}), **d) for d in staffprofile]    
    
       return Response(combined)


'''            Staff Profile Zone         '''
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

    def get(self, request, format=None):
        profile = StaffProfile.objects.all()
        serializer = StaffProfileSerializer(profile, many=True)
        return Response(serializer.data)
   
#Retrieve, update or delete a program instance. 
class StaffProfileUpdateView(APIView):
    serializer_class = StaffProfileSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return StaffProfile.objects.get(pk=pk)
        except StaffProfile.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        Staff_key = self.get_object(self.kwargs.get('pk_Staff', ''))
        serializer = self.serializer_class(Staff_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        profile = self.get_object(self.kwargs.get('pk_Staff', ''))
        serializer = StaffProfileSerializer(profile)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

