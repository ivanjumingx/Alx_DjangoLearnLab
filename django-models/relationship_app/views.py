from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Function-Based View for Listing Books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Displaying Library Details
@method_decorator(login_required, name='dispatch')
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
