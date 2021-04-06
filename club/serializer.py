from rest_framework import serializers

from club.models import *

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = "__all__"

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"
