from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # Retrieve all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a specific book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),   # Create a new book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update a specific book by ID
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a specific book by ID
]
