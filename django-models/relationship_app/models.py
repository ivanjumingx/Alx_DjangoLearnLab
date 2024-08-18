from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    books = models.ManyToManyField('Book', related_name='libraries', blank=True)
    librarian = models.OneToOneField('Librarian', on_delete=models.SET_NULL, null=True, blank=True, related_name='library')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"
