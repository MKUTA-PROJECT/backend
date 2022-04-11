from rest_framework import serializers

from lookup.models import *

class MemberRoleLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRoleLookup
        fields = "__all__"

class StaffRoleLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffRoleLookup
        fields = "__all__"

class LocationLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationLookup
        fields = "__all__"
