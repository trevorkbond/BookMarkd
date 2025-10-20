# API Documentation

## Base URL
```
http://localhost:5001/api
```

## Endpoints

### Health Check

#### GET `/api/health`

Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "message": "BookMarkd API is running"
}
```

---

### Books

#### GET `/api/books`

Get all books.

**Response:**
```json
{
  "books": [
    {
      "id": 1,
      "title": "Book Title",
      "author": "Author Name",
      "isbn": "1234567890123",
      "description": "Book description",
      "created_at": "2025-01-01T00:00:00",
      "updated_at": "2025-01-01T00:00:00"
    }
  ]
}
```

---

## Error Responses

All endpoints may return the following error responses:

### 404 Not Found
```json
{
  "error": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

---

## Future Endpoints (Planned)

- `POST /api/books` - Create a new book
- `GET /api/books/:id` - Get a specific book
- `PUT /api/books/:id` - Update a book
- `DELETE /api/books/:id` - Delete a book
- `POST /api/users` - Register a user
- `POST /api/auth/login` - User login
- `GET /api/users/:id/books` - Get user's books
- `POST /api/reviews` - Create a book review
- `GET /api/recommendations` - Get book recommendations
