# API Endpoints

1. GET /api/books/ - Retrieves all books
2. GET /api/books/<id>/ - Retrieves a specific book by ID
3. POST /api/books/create/ - Creates a new book (authenticated users only)
4. PUT /api/books/<id>/update/ - Updates a book (authenticated users only)
5. DELETE /api/books/<id>/delete/ - Deletes a book (authenticated users only)

# Permissions

- Unauthenticated users can view the list of books or retrieve a specific book.
- Only authenticated users can create, update, or delete books.
