from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List the fields to be displayed in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for easier navigation
    list_filter = ('author', 'publication_year')

    # Add a search bar to search through the title and author fields
    search_fields = ('title', 'author')
# Register your models here.
