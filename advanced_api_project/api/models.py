from django.db import models

class Author(models.Model):
    """
    The Author model represents an author, storing the author's name.
    Each author can be linked to multiple books (one-to-many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    The Book model represents a book, storing the book's title, publication year, and its author.
    Each book is linked to one author (many-to-one relationship).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
