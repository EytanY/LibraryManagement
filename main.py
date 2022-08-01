import datetime

from Model.Person import Person


if __name__ == '__main__':
    p = Person("Eytan", "Yegudayev", 316443878, datetime.date(1997, 3, 17))
    print(p)