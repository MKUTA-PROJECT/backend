from rest_framework import serializers

from club.models import *

class ClubSerializer(serializers.ModelSerializer):
    health_facility_name= serializers.ReadOnlyField(source='health_facility.get_name')
    class Meta:
        model = Club
        fields = "__all__"

class CSOSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSO
        fields = "__all__"
