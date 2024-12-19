from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer, UserFollowSerializer
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=400)
    

class loginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileView(APIView):
    def get(self, request):
        user = request.user
        return Response({"username": User.username, "email": User.email})
    

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            request.user.follow(user_to_follow)
            return Response({'detail': 'User followed successfully.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]


    def post(self, request, user_id):
        try:
           user_to_unfollow = CustomUser.objects.get(id=user_id)
           request.user.unfollow(user_to_unfollow)
           return Response({'detail': 'user unfollowed successfully.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'user not found.'}, status=status.HTTP_404_NOT_FOUND)
        

class UserListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserFollowSerializer
    queryset = CustomUser.objects.all()