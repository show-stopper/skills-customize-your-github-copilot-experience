from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str
    author: str


books: dict[int, Book] = {
    1: Book(title="The Hobbit", author="J. R. R. Tolkien"),
    2: Book(title="A Wrinkle in Time", author="Madeleine L'Engle"),
}


@app.get("/books")
def list_books() -> dict[int, Book]:
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    pass


@app.post("/books")
def create_book(book: Book) -> Book:
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book) -> Book:
    pass
