# query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"Author with name '{author_name}' does not exist."

# Sample Query 2: List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"Library with name '{library_name}' does not exist."

# Sample Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return f"Library with name '{library_name}' does not exist."
    except Librarian.DoesNotExist:
        return f"Librarian for library '{library_name}' does not exist."

if __name__ == '__main__':
    # Example usage
    print(get_books_by_author('John Doe'))
    print(list_books_in_library('Central Library'))
    print(get_librarian_for_library('Central Library'))
