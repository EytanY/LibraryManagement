import datetime

from Model.Borrow import Borrow
from Model.Person import Person


class Customer(Person):

    def __init__(self, first_name, last_name, pid, birth, email, phone):
        super().__init__(first_name, last_name, pid, birth)
        self.email = email
        self.phone = phone
        self.current_borrows = []
        self.last_borrows = []

    def addBorrow(self, book, end_date):
        self.current_borrows.append(Borrow(book, datetime.date.today(), end_date))
        return

    def returnBook(self, book):
        if book in self.current_borrows:
            self.current_borrows.remove(book)
            return True
        return False
