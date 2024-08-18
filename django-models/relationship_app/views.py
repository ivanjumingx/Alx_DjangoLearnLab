from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

# Function-Based View for Listing Books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-Based View for Displaying Library Details
@method_decorator(login_required, name='dispatch')  # Ensure only authenticated users can access this view
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
            user = form.save()
            auth_login(request, user)  # Log in the user after registration
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Utility function to check user role
def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'

# Admin View
@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@login_required
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@login_required
@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Function-Based View for Adding a Book (requires permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        # Logic to add a book
        pass
    return render(request, 'relationship_app/add_book.html')

# Function-Based View for Changing a Book (requires permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        # Logic to change a book
        pass
    return render(request, 'relationship_app/change_book.html', {'book': book})

# Function-Based View for Deleting a Book (requires permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')  # Redirect after deletion
    return render(request, 'relationship_app/delete_book.html', {'book': book})