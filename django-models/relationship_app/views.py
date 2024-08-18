from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

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

# Function-Based View for User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('list_books')  # Redirect to a page after login
        else:
            return HttpResponse("Invalid login")
    return render(request, 'relationship_app/login.html')

# Function-Based View for User Logout
@login_required
def user_logout(request):
    auth_logout(request)
    return render(request, 'relationship_app/logout.html')

# Function-Based View for User Registration
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})