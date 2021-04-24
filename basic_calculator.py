from tkinter import *
from functools import partial  # allow function with parameter in Button
import string
import funcs as fc  # my module :)


class BasicCalculator:

    def __init__(self):
        self.window1 = Tk()
        self.window1.title("Calculator")
        self.window1.geometry("600x800")
        self.window1.minsize(480, 770)
        self.window1.config(bg="#303133")

        self.char_list = ["%", "", "", "", "(", ")", "C", "+", "7", "8", "9", "-", "4", "5", "6", "*", "1", "2", "3", "/", "<-", "0", ".", "="]
        self.operators_allowed = r"""+-*/%"""
        self.index = 0

        self.buttons_frame = Frame(self.window1, bg="#303133")

        self.create_widgets()

        self.buttons_frame.pack(side=BOTTOM)

        self.window1.mainloop()

    def back(self):  # function who will bring the user to the main window (MainApp)
        self.window1.destroy()
        from main import MainApp
        MainApp()

    def touch_command(self, touch):
        if touch == "<-":
            self.entry.delete(len(self.entry.get()) - 1, END)
            return
        elif touch == "=":
            self.execute()
            return
        elif touch == "C":
            self.clear()
            return

        self.entry.insert(END, touch)

    def execute(self):  # execute the calcul
        self.to_execute = str(self.entry.get()).strip().replace(" ", "")
        self.entry.delete(0, END)
        try:                                                # Verify if the input can't be evaluated
            self.entry.insert(0, eval(self.to_execute))
        except:
            if fc.str1_in_str2(string.ascii_letters, self.to_execute):  # Verify if the input contains letters
                self.entry.insert(0, "Enter numbers and operators only")
            elif fc.str1_in_str2(fc.bad_pow, self.to_execute):  #"²" in self.to_execute
                self.entry.insert(0, "Use two multiply symbols (**) for power")

    def clear(self):
        self.entry.delete(0, END)

    def create_widgets(self):
        self.create_image()
        self.create_buttons()
        self.create_entry()

    def create_image(self):
        self.back_image = PhotoImage(file="img/transparent_back.png").subsample(3, 3)

    def create_entry(self):  # this is where the calcul will be write
        self.entry = Entry(self.window1, font="Helvetica 20", bg="#262729", fg="#ECB613", insertbackground="#ECB613",
                           relief="flat", cursor="pencil")
        self.entry.pack(fill=X, pady=(100, 0))

    def create_buttons(self):  # function who creates all buttons (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -, *, /, =)
        self.back_button = Button(self.window1, image=self.back_image, bg="#303133", bd=0, highlightthicknes=0, activebackground="#262729", command=self.back)
        self.back_button.place(width=80, height=80)

        for rowx in range(1, 7):
            for columnx in range(1, 5):
                if self.char_list[self.index] == "":
                    self.index += 1
                    continue

                self.n0 = Button(self.buttons_frame, text=self.char_list[self.index], font="Helvetica 14", bg="#262729",
                                 fg="#ECB613", width=10, height=4, activebackground="#ECB613",
                                 command=partial(self.touch_command, self.char_list[self.index]))
                self.n0.grid(row=rowx, column=columnx)
                self.index += 1


# o5lh = Calculator()
# o5lh.window.mainloop()
