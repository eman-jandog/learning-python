class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"


class FictionBook(Book):
    genre = 'Fiction'

    def __init__(self, title, author):
        super().__init__(title, author)

    def describe(self):
        return f"{self.title}({self.genre}) by {self.author}"
    