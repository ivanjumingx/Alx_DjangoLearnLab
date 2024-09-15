# blog/urls.py
from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView,
    PostDeleteView, add_comment, CommentUpdateView, CommentDeleteView,
    search_posts, tagged_posts, PostByTagListView
)

urlpatterns = [
    # User management
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog post management
    path('post/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment management
    path('post/<int:pk>/comments/new/', add_comment, name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # Search and tagging
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', tagged_posts, name='tagged_posts'),  # Updated tag route

    # URL pattern for posts by tag
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
