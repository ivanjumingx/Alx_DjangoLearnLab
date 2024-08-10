# Django Admin Interface Configuration for Book Model

## Registering the Model

In `bookshelf/admin.py`, the `Book` model was registered with Django admin:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
