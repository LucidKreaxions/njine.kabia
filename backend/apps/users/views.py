from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, RegisterSerializer

# Create your views here.
#Register View
class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


#Login View
class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=400)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        })

# Profile View
class ProfileView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        serializer = UserSerializer(request.user)
        return Response(serializer.data)
