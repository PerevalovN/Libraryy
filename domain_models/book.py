class Book:

    def __init__(self, title: str, year: int, author: str):
        self.title = title
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.title}, {self.year}, {self.author}'

    def __repr__(self):
        return f'{self.title}, {self.year}, {self.author}'


class BookQueryResult:
    def __init__(self, book: Book, book_id: int):
        self.book = book
        self.book_id = book_id
