from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title is required.')
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError('Author is required.')
        return author

    def clean_publication_year(self):
        publication_year = self.cleaned_data.get('publication_year')
        if publication_year and publication_year < 1900:
            raise forms.ValidationError('Publication year must be after 1900.')
        return publication_year
