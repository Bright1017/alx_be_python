class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checkedout = False
    
    def check_out(self):
        """Marks the book as checked out."""
        if self._is_checkedout:
            # If the book is already checked out, return False
            return False
        else:
            # If the book is not checked out, mark it as checked out and return True
            self._is_checkedout = True
            return True
    
    def return_book(self):
        """Marks the book as returned."""
        if not self.check_out:
            return False
        else:
            self._is_checkedout = False
            return True
    
    def is_available(self):
        """Returns True if the book is available for check-out."""
        return not self._is_checkedout
    



class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Adds a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only instances of Book can be added.")
            
    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Book '{title}' has been checked out.")
                return
            print(f"Book '{title}' is not available for check-out.")
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Book '{title}' has been returned.")
                return
            print(f"Book '{title}' was not checked out.")
    
    def list_available_books(self):
        """Lists all available books in the library."""
        for book in self._books:
            if book.is_available():
                print("Here are the available books in the library:")
                print(f"Title: {book.title}, Author: {book.author}")
            else:
                print("No books are currently available.")
    

        
            
    



# book1 = Book("EZE goes to school", "John Doe")
# book2 = Book("Brave New World", "Aldous Huxley")
# book3 = Book("1984", "George Orwell")
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# library.check_out_book(book1.title)
# print(library._books)