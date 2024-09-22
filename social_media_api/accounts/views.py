from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
from .models import CustomUser

CustomUser = get_user_model()

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class FollowUser(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # Ensures all users are available for follow/unfollow
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(self.queryset, id=user_id)  # Use queryset to retrieve users
        if target_user != request.user:
            request.user.followers.add(target_user)  # Add the user to the current user's following list
            return Response({"message": "User followed successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUser(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # Ensures all users are available for unfollowing
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(self.queryset, id=user_id)  # Use queryset to retrieve users
        if target_user != request.user:
            request.user.followers.remove(target_user)  # Remove the user from the current user's following list
            return Response({"message": "User unfollowed successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)