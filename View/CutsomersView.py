from tkinter import Button
from tkinter.ttk import *
from View import View
from tkinter import Entry, Label
from tkcalendar import Calendar


class CustomersView(View):
    def __init__(self):
        super().__init__()


        title = Label(self.root, text="Customers")
        title.config(font=("Courier", 34))
        title.pack()

        enter_first_name_txt = Label(self.root, text="Enter First Name:")
        enter_first_name_txt.config(font=("Courier", 14))
        enter_first_name_txt.pack()

        self.customer_first_name = Entry()
        self.customer_first_name.pack()

        enter_last_name_txt = Label(self.root, text="Enter Last Name:")
        enter_last_name_txt.config(font=("Courier", 14))
        enter_last_name_txt.pack()

        self.customer_last_name = Entry()
        self.customer_last_name.pack()

        enter_id_txt = Label(self.root, text="Enter ID:")
        enter_id_txt.config(font=("Courier", 14))
        enter_id_txt.pack()

        self.customer_id = Entry()
        self.customer_id.pack()

        enter_email_txt = Label(self.root, text="Enter Email:")
        enter_email_txt.config(font=("Courier", 14))
        enter_email_txt.pack()

        self.customer_email = Entry()
        self.customer_email.pack()

        enter_phone_txt = Label(self.root, text="Enter Phone Number:")
        enter_phone_txt.config(font=("Courier", 14))
        enter_phone_txt.pack()

        self.customer_phone = Entry()
        self.customer_phone.pack()

        enter_birth_txt = Label(self.root, text="Enter Birthdate:")
        enter_birth_txt.config(font=("Courier", 14))
        enter_birth_txt.pack()

        cal = Calendar(self.root, selectmode='day', year=2020, month=5, day=22)
        cal.pack()

        # Add Customer Button
        self.add_customer_btn = Button(self.root, text='Add New Customer', pad=(30, 5))
        self.add_customer_btn.pack(pady=5)
        # Return Menu
        self.menu_btn = Button(self.root, text='Menu', pad=(30, 5))
        self.menu_btn.pack(pady=5)


    def show(self):
        self.root.mainloop()

    def addCustomer(self):
        pass



