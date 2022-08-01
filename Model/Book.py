from Author import Author

categories = ["Drama", "Action", "Fantasy", "Novel"]
serial_number = 3000


class Book:
    global serial_number

    def __init__(self, name, category, publication_date, author: Author):
        self.name = name
        self.category = category
        self.publication_date = publication_date
        self.author = author
        self.serial_number = serial_number
        self.available = True

    def __eq__(self, other):
        if isinstance(other, Book):
            return other.serial_number == self.serial_number

    def __str__(self):
        return f"Name:{self.name}  Author:{self.author.first_name} {self.author.last_name}  Category:{self.category}  Publication Date:{self.publication_date}"

