from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from member.models import Member
from member.serializer import MemberSerializer
from member.views import MemberView
from project.models import Project
from project.serializer import ProjectSerializer

# Create your views here.
'''            Project Zone         '''


class ProjectView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

# Retrieve, update or delete a program instance.


class ProjectUpdateView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        project_key = self.get_object(self.kwargs.get('pk_project', ''))
        serializer = self.serializer_class(project_key, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_201_CREATED
            serializer.save()
            return Response(serializer.data, status=status_code)

    def get(self, request, *args, **kwargs):
        project = self.get_object(self.kwargs.get('pk_project', ''))
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''            Members of specific Project         '''


class ProjectMemberView(APIView):
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]

    def get_object(self, pk):  # Query a member of a given club id
        try:
            return MemberView.objects.filter(memberProfile__project=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        serializer = {}
        member = self.get_object(self.kwargs.get('pk_project', ''))
        member = MemberSerializer(member, many=True).data

        return Response(member)
