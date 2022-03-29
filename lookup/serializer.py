from rest_framework import serializers

from lookup.models import *

class MemberRoleLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRoleLookup
        fields = "__all__"

# class ClubSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Club
#         fields = "__all__"
