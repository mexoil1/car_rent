from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    '''Serializer for user'''
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email')


class UserRegisterSerializer(serializers.ModelSerializer):
    '''Serialzier for user register'''
    class Meta:
        model = User
        fields = ['email', 'first_name',
                  'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
