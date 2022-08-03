from tkinter import *
from tkinter.ttk import Style


class View:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x620')

        # Create style Object
        self.style = Style()
        self.style.configure('TButton', font=('calibri', 20, 'bold'),borderwidth='4')


        # Changes will be reflected
        # by the movement of mouse.
        self.style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

