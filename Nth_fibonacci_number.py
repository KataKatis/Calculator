from tkinter import *


class NthFibNumber:

    def __init__(self):
        self.window3 = Tk()
        self.window3.title("The Millionth Fibonacci Number")
        self.window3.geometry("800x800")
        self.window3.config(bg="#303133")  # window background color

        self.create_widgets()

        self.window3.mainloop()

    def back(self):  # function who will bring the user to the main window (MainApp)
        self.window3.destroy()
        from main import MainApp
        MainApp()

    def create_widgets(self):
        self.create_image()
        self.create_button()

    def create_image(self):
        self.back_image = PhotoImage(file="img/transparent_back.png").subsample(3, 3)  # importing the back image (to MainApp)

    def create_button(self):
        self.back_button = Button(self.window3, image=self.back_image, bg="#303133", bd=0, highlightthicknes=0, activebackground="#262729", command=self.back)
        self.back_button.place(width=80, height=80)

        self.info = Button(self.window3, text="?", font="Helvetica 11", bg="#303133", fg="#ECB613", activebackground="#ECB613", bd=0, width=3)
        self.info.pack(side=RIGHT, anchor=N)
