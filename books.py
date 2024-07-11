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
