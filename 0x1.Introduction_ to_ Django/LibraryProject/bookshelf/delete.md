# Delete Operation

## Command Used:
```python
from bookshelf.models import Book
# Retrieve the book with the title "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the book
book.delete()
# Verify deletion by trying to retrieve the book again
try:
    book = Book.objects.get(title="Nineteen Eighty-Four")
    print("Book still exists:", book)
except Book.DoesNotExist:
    print("Book successfully deleted.")
