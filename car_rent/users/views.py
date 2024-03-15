from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from .serializers.model_serializers import (UserRegisterSerializer,
                                            UserSerializer)
from .serializers.serializers import (AuthTokenSerializer,
                                      UpdatePasswordSerializer)
from .utils import authenticate_user, update_password

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

        user = authenticate_user(email, password)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=status.HTTP_202_ACCEPTED)


class UpdatePasswordView(APIView):
    '''Update Password'''
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = UpdatePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # TODO: add email message and code
        email = serializer.validated_data.get('email')
        new_password = serializer.validated_data.get('new_password')
        if request.user.email == email:
            update_password(email, new_password)
            return Response({'message': 'Password successfully updated'}, status=status.HTTP_200_OK)
        raise PermissionDenied()
