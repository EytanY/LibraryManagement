from datetime import date


class Person:

    def __init__(self, first_name, last_name, pid, birth):
        self.first_name = first_name
        self.last_name = last_name
        self.pid = pid
        self.birthdate = birth

    def __str__(self):
        return f"Name:{self.first_name} {self.last_name}    ID:{self.pid}    Age:{self.getAge()}"


    def __eq__(self, other):
        if isinstance(other, Person):
            return other.pid == self.pid
        return False


    def getAge(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

