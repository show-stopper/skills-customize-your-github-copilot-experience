# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that manages a collection of books. You will practice defining API routes, validating request data with Pydantic models, and returning appropriate HTTP responses.

## 📝 Tasks

### 🛠️ Create API Routes

#### Description

Use the provided starter code to create a FastAPI application for a book collection. Add routes that allow clients to retrieve all books and retrieve one book by its ID.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Define a `GET /books` route that returns the complete collection.
- Define a `GET /books/{book_id}` route that returns the requested book.
- Return a `404` response when a requested book ID does not exist.
- Start successfully with the FastAPI development server.

### 🛠️ Add Create and Update Operations

#### Description

Expand the API so clients can add new books and update existing books. Use a Pydantic model to validate the data received in request bodies.

#### Requirements

Completed program should:

- Define a Pydantic model with required `title` and `author` fields.
- Define a `POST /books` route that accepts a validated book and adds it to the collection.
- Return the newly created book from the `POST /books` route.
- Define a `PUT /books/{book_id}` route that updates an existing book.
- Return a `404` response when an update targets a book ID that does not exist.
- Reject requests that omit required book fields.

### 🛠️ Test the API

#### Description

Run the API locally and use the automatically generated FastAPI documentation to test each route.

#### Requirements

Completed program should:

- Run the application with a command such as `uvicorn starter-code:app --reload`.
- Open the interactive documentation at `/docs`.
- Successfully test `GET`, `POST`, and `PUT` requests from the documentation page.
- Demonstrate both a successful request and a `404` response for an unknown book ID.

For example, a valid request to create a book could be:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```
