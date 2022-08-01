from Model.Book import Book
from Model.Person import Person


class Author(Person):
    def __init__(self, first_name, last_name, pid, birth):
        super().__init__(first_name, last_name, pid, birth)
        self.books = []

    def addBook(self, book: Book):
        self.books.append(book)
        return True

    def printAllBook(self):
        for book in self.books:
            print(book)

