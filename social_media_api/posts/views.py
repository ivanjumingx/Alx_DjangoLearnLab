from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from accounts.models import CustomUser
from notifications.models import Notification

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


class LikePost(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to safely retrieve the post or return a 404 error if not found
        post = generics.get_object_or_404(Post, pk=pk)

        # Use get_or_create to like the post, ensuring no duplicate likes
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"message": "You've already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post
        )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePost(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to retrieve the post
        post = generics.get_object_or_404(Post, pk=pk)

        # Try to retrieve the like and delete it
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"error": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)

