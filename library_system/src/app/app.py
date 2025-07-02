from module.library import Library
from module.book import Book, FictionBook
import os

library = Library()

def main():
    choice = 'y'
    while choice != 'n':
        interface = 'Library System \n(a) - Add book\n(f) - Add fiction book\n(r) - Remove book\n(l) - List books\n(e) - Exit\n'
        print(interface)
        choice = input('Enter selection: ')

        match choice:
            case 'a':
                title = input('Enter book title: ')
                author = input('Enter book author: ')
                book = Book(title, author)
                library.add_book(book)
            case 'f':
                title = input('Enter book title: ')
                author = input('Enter book author: ')
                book = FictionBook(title, author)
                library.add_book(book)
            case 'r':
                title = input('Enter book title to remove: ')
                library.remove_book(title)
            case 'l':
                library.list_books()
            case 'e':
                return

        choice = input('Continue? ')
        while choice != 'y':
            choice = input('Continue? ')
        
if __name__ == '__main__':
    main()