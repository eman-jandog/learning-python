
# Create books and library
book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()