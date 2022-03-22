from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from account.models import *


class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    


    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials ")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.roles,
                'name': user.get_full_name(),
                'id': user.id
            }

            return validation
        except user.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials ")



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'first_name': 'The First Name should only contain alphanumeric characters',
        'last_name': 'The Last Name should only contain alphanumeric characters'
        }

    class Meta:
        model = CustomUser
        fields = ['email','phone', 'roles', 'password', 'first_name', 'last_name','middle_name','sex']

    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        roles = attrs.get('roles', '')

       
        if not first_name.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages['first_name'])
        if not last_name.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages['last_name'])
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
