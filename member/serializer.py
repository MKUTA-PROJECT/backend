from rest_framework import serializers
from member.models import *
from account.models import CustomUser

class MemberProfileSerializer(serializers.ModelSerializer):
    club_name= serializers.ReadOnlyField(source='club.get_name')
    role_name= serializers.ReadOnlyField(source='role.get_name')
    class Meta:
        model = MemberProfile
        fields = "__all__"

class MemberContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberContribution
        fields = "__all__"


# get a few fields from the user model and use them to display the club members
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email','sex','date_joined', 'phone']

    def create(self, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)