from rest_framework import serializers

from staff.models import *

class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = "__all__"