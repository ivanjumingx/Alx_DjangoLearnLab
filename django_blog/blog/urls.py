# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog post management
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View a specific post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # Update a specific post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete a specific post
    path('', views.PostListView.as_view(), name='post_list'),  # List all posts (usually the homepage or a dedicated posts page)
]

