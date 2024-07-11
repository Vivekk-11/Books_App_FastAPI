from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Book One", "author": "Author One", "category": "science"},
    {"title": "Book Two", "author": "Author Two", "category": "science"},
    {"title": "Book Three", "author": "Author Three", "category": "history"},
    {"title": "Book Four", "author": "Author Four", "category": "math"},
    {"title": "Book Five", "author": "Author Five", "category": "math"},
    {"title": "Book Six", "author": "Author Two", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title):
    for book in BOOKS:
        if book.get("title").casefold == book_title.casefold():
            return book


@app.get("/books/")
async def read_book_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_book_by_category_and_author(book_author, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author and book.get("category") == category.casefold():
            books_to_return.append(book)
    return books_to_return
