from Model.Author import Author
from Model.Book import Book
from Model.Borrow import Borrow
from Model.Customer import Customer


class Library:

    def __init__(self, name):
        self.name = name
        self.customers = set()
        self.books = set()
        self.authors = set()
        self.current_borrows = set()
        self.last_borrows = set()

    def addCustomer(self, customer: Customer):
        self.customers.add(customer)

    def addBook(self, book: Book):
        self.books.add(book)

    def addAuthor(self, author: Author):
        self.authors.add(author)

    def addBorrow(self, borrow: Borrow):
        self.current_borrows.add(borrow)

    def returnBorrow(self, borrow: Borrow):
        self.current_borrows.remove(borrow)
        self.last_borrows.add(borrow)

    def printAllCustomers(self):
        for customer in self.customers:
            print(customer)