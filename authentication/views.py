from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError

from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer

class ObtainTokenPariWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
            except IntegrityError as e:
                return Response("Test",status=status.HTTP_406_NOT_ACCEPTABLE,)
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        print("DEBUG: ", request.data)
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Successful Logout", status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class DummyProtectedView(APIView):

    def get(self, request):
        return Response(data={"Authenticated Inside":"Auth"}, status=status.HTTP_200_OK)

class UnprotectedView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        print("Inside")
        return Response(data={"Unprotected":"No Auth needed"}, status=status.HTTP_200_OK)