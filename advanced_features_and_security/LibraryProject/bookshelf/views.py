from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book

# View for listing books
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'books/book_list.html', {'books': books})

# View for adding a book (requires 'can_create' permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        # Logic for adding a book
        pass
    return render(request, 'books/add_book.html')

# View for editing a book (requires 'can_edit' permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Logic for editing the book
        pass
    return render(request, 'books/edit_book.html', {'book': book})

# View for deleting a book (requires 'can_delete' permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

# Handle permission errors
def handle_permission_error(request):
    return HttpResponseForbidden("You do not have permission to perform this action.")
