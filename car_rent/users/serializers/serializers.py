from rest_framework import serializers

from .model_serializers import UserSerializer


class AuthTokenSerializer(serializers.Serializer):
    '''Serializer for Login'''
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class UpdatePasswordSerializer(serializers.Serializer):
    '''Serializer for updating password'''
    email = serializers.EmailField(required=True)
    new_password = serializers.CharField(required=True)


class AuthTokenOutputSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)
    access = serializers.CharField(required=True)
    user = UserSerializer()
