class Book:
    def __init__(self, title: str, author: str):
        """Initializes a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes an EBook instance with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"

class Library:
    def __init__(self):
        """Initializes a Library instance to store a collection of books."""
        self.books = []

    def add_book(self, book: Book):
        """Adds a book to the library."""
        self.books.append(book)
        print(f"Added: {book}")

    def list_books(self):
        """Lists all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)