from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model, handling all fields including custom validation.
    The publication year cannot be in the future.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for the publication year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model, including a nested BookSerializer to serialize
    related books. This dynamically includes all books related to an author.
    """
    # Nested serializer to serialize related books dynamically
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
