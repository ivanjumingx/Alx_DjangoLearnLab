from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import CustomUser

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user  # Get the authenticated user

        # Get all users the current user is following
        following_users = user.following.all()  # Use following.all() to get the list of followed users

        # Filter posts from users the current user is following, ordered by creation date (latest first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Prepare the response data
        post_data = [
            {
                "id": post.id,
                "author": post.author.username,
                "title": post.title,
                "content": post.content,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
            }
            for post in posts
        ]

        return Response(post_data, status=status.HTTP_200_OK)

