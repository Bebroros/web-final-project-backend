from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from user_auth.models import CustomUser
from user_auth import permissions as user_auth_permissions
from .serializers import UserSerializer, UserProfileSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


class CustomUserRegister(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:3000"


class UserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        if request.user.id != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = CustomUser.objects.get(pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        if request.user.id != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = CustomUser.objects.get(pk=pk)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
