from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Book, Library
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Function-Based View for Listing Books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Displaying Library Details
@method_decorator(login_required, name='dispatch')  # Ensure only authenticated users can access this view
class LibraryDetailView(DetailView):
    model = Library  # Model to use for this view
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # Name to use for the object in the template
