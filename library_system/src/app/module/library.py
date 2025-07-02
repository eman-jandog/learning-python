class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for index, book in enumerate(self.books):
            if book.title == title:
                self.books.pop(index)

    def list_books(self):
        if len(self.books) == 0: 
            print('No books added.')
        else:
            for book in self.books:
                print(book.describe())