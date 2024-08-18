import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

# Example usage
if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':")
    for book in books_by_author('J.K. Rowling'):
        print(book.title)

    print("\nBooks in Library 'Central Library':")
    for book in books_in_library('Central Library'):
        print(book.title)

    print("\nLibrarian for 'Central Library':")
    librarian = librarian_for_library('Central Library')
    print(librarian.name)
