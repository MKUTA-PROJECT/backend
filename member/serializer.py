from rest_framework import serializers

from member.models import *

class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberProfile
        fields = "__all__"