# Update Operation

## Command Used:
```python
from bookshelf.models import Book
# Retrieve the book with the title "1984"
book = Book.objects.get(title="1984")
# Update the title of the book
book.title = "Nineteen Eighty-Four"
# Save the changes
book.save()
# Print the updated title
print(book.title)
