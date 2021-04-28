from tkinter import *
import funcs as fc


class NthFibNumber:

    def __init__(self):
        self.window3 = Tk()
        self.window3.title("The Millionth Fibonacci Number")
        self.window3.geometry("800x800")
        self.window3.config(bg="#303133")  # window background color

        self.frame = Frame(self.window3, bg="#303133")

        self.create_widgets()

        self.frame.pack(expand=YES)

        self.window3.mainloop()

    def back(self):  # function who will bring the user to the main window (MainApp)
        self.window3.destroy()
        from main import MainApp
        MainApp()

    def found(self):
        self.nth = int(self.entry_nth.get())
        self.result["state"] = "normal"
        self.result.delete(0, END)
        self.result.insert(0, fc.fib(self.nth))
        self.result["state"] = "readonly"

    def create_widgets(self):
        self.create_image()
        self.create_entry()
        self.create_button()

    def create_image(self):
        self.back_image = PhotoImage(file="img/transparent_back.png").subsample(3, 3)  # importing the back image (to MainApp)

    def create_entry(self):
        self.entry_nth = Entry(self.frame, bg="#262729", fg="#ECB613", font="Helvetica 20", justify="center")
        self.entry_nth.grid(row=1, column=1)

        self.result = Entry(self.frame, state="readonly", readonlybackground="#262729", fg="#ECB613", font="Helvetica 20", justify="center")
        self.result.grid(row=3, column=1)

    def create_button(self):
        self.back_button = Button(self.window3, image=self.back_image, bg="#303133", bd=0, highlightthicknes=0, activebackground="#262729", command=self.back)
        self.back_button.place(width=80, height=80)

        self.found = Button(self.frame, text="Found", font="Helvetica 15", bg="#262729", fg="#ECB613", command=self.found)
        self.found.grid(row=2, column=1, pady=(20, 20))
