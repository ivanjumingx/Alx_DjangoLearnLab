from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FeedView
from .views import LikePost, UnlikePost

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user_feed'),
    path('posts/<int:pk>/like/', LikePost.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePost.as_view(), name='unlike_post'),
]
