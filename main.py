from tkinter import *
from functools import partial


class MainApp:

    def __init__(self):
        self.window = Tk()  # window creation
        self.window.title("Main Display")  # window title
        self.window.geometry("500x500")  # window geometry
        self.window.minsize(500, 500)
        self.window.maxsize(500, 500)
        self.window.config(bg="#303133")  # window background color

        self.windows = ["Basic calculator", "Length convertor", "The Nth Fibonacci number"]

        self.create_widgets()  # widgets creation

        self.window.mainloop()

    def create_windows(self, mode):  # opening of windows by buttons
        if mode == "Basic calculator":  # open the basic calculator
            self.window.destroy()
            from basic_calculator import BasicCalculator
            BasicCalculator()
        elif mode == "Length convertor":  # open the length convertor
            self.window.destroy()
            from length_conversion import LengthConvertor
            LengthConvertor()
        elif mode == "The Nth Fibonacci number":
            self.window.destroy()
            from Nth_fibonacci_number import NthFibNumber
            NthFibNumber()

    def create_widgets(self):  # calling functions who create widgets
        self.create_title()
        self.create_buttons()

    def create_title(self):
        self.title = Label(self.window, text="Which calculator do you want ?", font="Helvetica 22", bg="#303133", fg="#ECB613")
        self.title.pack(pady=(15, 25))

    def create_buttons(self):  # these buttons are going to open new windows
        for i in self.windows:
            self.change_window = Button(self.window, text=i, font="Helvetica 15", bg="#262729", fg="#ECB613", relief="flat", activebackground="#ECB613", bd=0, command=partial(self.create_windows, i))
            self.change_window.pack(fill=X)  # button to open the basic calculator


app = MainApp()

