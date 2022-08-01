import datetime

from Book import Book
from Model.Customer import Customer

serial_number = 1000


class Borrow:

    def __init__(self, book: Book, customer: Customer, start_date, end_date):
        global serial_number
        self.book = book
        self.start_date = start_date
        self.end_date = end_date
        self.serial_number = serial_number
        self.customer = customer
        serial_number += 1
        book.available = False



    def isLateReturn(self):
        return datetime.date.today() > self.end_date

    def __eq__(self, other):
        if isinstance(other, Borrow):
            return other.serial_number == self.serial_number
        return False

    def __str__(self):
        return f"Serial Number:{self.serial_number}  Book:{self.book.name}  Start Date:{self.start_date}  End Date:{self.end_date}"

