from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book, Author
from api.serializers import BookSerializer


class BookTests(APITestCase):

    def setUp(self):
        # Create an author and a book to be used in tests
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(
            title="Animal Farm", publication_year=1945, author=self.author)
        self.book_list_url = reverse('book-list')  # URL for list view



    def test_create_book(self):
        data = {
            "title": "Brave New World",
            "publication_year": 1932,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_retrieve_single_book(self):
        book_detail_url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")


    def test_update_book(self):
        book_detail_url = reverse('book-detail', args=[self.book.id])
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }
        response = self.client.put(book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")


    def test_delete_book(self):
        book_detail_url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    def test_filter_books_by_title(self):
        response = self.client.get(self.book_list_url, {'title': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")


    def test_search_books_by_author(self):
        response = self.client.get(self.book_list_url, {'search': 'George Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_order_books_by_publication_year(self):
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Animal Farm")  # Published earlier
        self.assertEqual(response.data[1]['title'], "1984")


