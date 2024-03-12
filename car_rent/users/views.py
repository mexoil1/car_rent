from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from .serializers.model_serializers import (UserRegisterSerializer,
                                            UserSerializer)
from .serializers.serializers import (AuthTokenSerializer,
                                      UpdatePasswordSerializer)

User = get_user_model()


class RegistrationView(APIView):
    '''Registration'''

    def post(self, request):
        user_data = request.data.copy()
        serializer = UserRegisterSerializer(data=user_data)
        if serializer.is_valid():
            # TODO: add smtp mail for checking email
            serializer.save()
            return Response(
                {'message': 'User have been registered successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(TokenViewBase):
    '''Authorization'''

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = self.authenticate_user(email, password)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=status.HTTP_202_ACCEPTED)

    def authenticate_user(self, email, password):
        '''Authorize user'''
        user = get_object_or_404(User, email=email)
        authenticated_user = authenticate(
            username=user.username, password=password)
        if authenticated_user is None:
            raise AuthenticationFailed('Invalid password')
        return authenticated_user


class UpdatePasswordView(APIView):
    '''Update Password'''

    def patch(self, request):
        serializer = UpdatePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # TODO: add email message and code
        email = serializer.validated_data.get('email')
        new_password = serializer.validated_data.get('new_password')

        self.update_password(email, new_password)

        return Response({'message': 'Password successfully updated'}, status=status.HTTP_200_OK)

    def update_password(self, email, new_password):
        '''Updating password'''
        user = get_object_or_404(User, email=email)
        user.password = make_password(new_password)
        user.save()
