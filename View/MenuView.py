from tkinter import Button
from tkinter.ttk import *
from View import View
from PIL import Image, ImageTk


class MenuView(View):
    def __init__(self):
        super().__init__()


        # title "Library Management System"
        title_txt = Label(self.root, text="Library Management")
        title_txt.config(font=("Courier", 30))
        title_txt.pack()

        # Load the image
        image = Image.open('../Img/menu_books.png')
        img = image.resize((100, 100))
        self.img = ImageTk.PhotoImage(img)
        label = Label(self.root, image=self.img)
        label.pack()

        # button customers
        self.customers_btn = Button(self.root, text='Customers', command=self.openCustomersView, pad=(50, 10))
        self.customers_btn.pack()

        # button authors
        self.authors_btn = Button(self.root, text='Authors', command=self.openCustomersView, pad=(50, 10))
        self.authors_btn.pack(pady=10)

        # button books
        self.books_btn = Button(self.root, text='Books', command=self.openCustomersView, pad=(50, 10))
        self.books_btn.pack(pady=10)

        # button borrows
        self.borrows_btn = Button(self.root, text='Borrow', command=self.openCustomersView, pad=(50, 10))
        self.borrows_btn.pack(pady=10)

        # button reports
        self.reports_btn = Button(self.root, text='Reports', command=self.openCustomersView, pad=(50, 10))
        self.reports_btn.pack(pady=10)

        # button exit
        self.exit_btn = Button(self.root, text='Exit & Save', command=self.exitAndSave, pad=(50, 10))
        self.exit_btn.pack(pady=10)

    def openCustomersView(self):
        pass

    def show(self):
        self.root.mainloop()

    def exitAndSave(self):
        self.root.destroy()


MenuView().show()
