from tkinter import *


class LengthConvertor:

    def __init__(self):
        self.window2 = Tk()  # window creation
        self.window2.title("Length convertor")  # title of the window
        self.window2.geometry("1000x700")  # size of the window
        self.window2.config(bg="#303133")  # background
        self.unite_of_measure = ["km", "hm", "m", "dm", "cm", "mm"]  # unit_of_measure

        self.main_frame = Frame(self.window2, bg="#303133")  # this frame will contains all widgets
        self.left_frame = Frame(self.main_frame, bg="#303133")  # this frame contains the start value
        self.right_frame = Frame(self.main_frame, bg="#303133")  # this frame contains the final value (after conversion)

        self.frames = [self.left_frame, self.right_frame]  # list of the two frames
        self.pow_units = {  # the meter is the main unite of measure
            "km": 10**-3,
            "hm": 10**-2,
            "dam": 10**-1,
            "m": 10**0,
            "dm": 10**1,
            "cm": 10**2,
            "mm": 10**3
        }

        self.create_widgets()

        self.left_frame.grid(row=1, column=1)  # print (not in console) both frames
        self.right_frame.grid(row=1, column=3)  # print (not in console) both frames
        self.main_frame.pack(expand=YES)

        self.window2.mainloop()

    def back(self):  # function who will bring the user to the main window (MainApp)
        """This function quit the Length convertor of come again to the main app"""
        self.window2.destroy()
        from main import MainApp
        MainApp()

    def convert(self):
        """The mission of this function is to convert what the user want to convert."""
        if "." in self.entry1.get():                                    #
            try:                                                        #
                self.value_to_convert = float(self.entry1.get())  # take the value (not the unite) which will be convert
            except:                                                     #
                self.entry2.delete(0, END)                              #
                self.entry2.insert(0, "Enter only integers or float")   # This block just verify if the user input contains forbidden characters
                return                                                  #
        else:                                                           #
            try:                                                        #
                self.value_to_convert = int(self.entry1.get())  # take the value (not the unite) which will be convert
            except:                                                     #
                self.entry2.delete(0, END)                              #
                self.entry2.insert(0, "Enter only integers or float")   #
                return                                                  #

        self.new_power = self.pow_units[self.unitevar2.get()] * (1/self.pow_units[self.unitevar1.get()])  # coefficient who will multiply self.value_to_convert

        self.result = "{:.20f}".format(self.value_to_convert * self.new_power)  # I put the result (the converted value) in this variable to avoid the scientific notation
        self.result = self.result.rstrip("0")  # I remove all useless 0
        if self.result[-1] == ".":
            self.result = self.result.replace(".", "")  # here I verify if the number is for example "1200.", if True : I remove the "." at the end (it is useless and ugly)

        self.entry2.delete(0, END)  # delete the content of the entry in which the result will be print
        self.entry2.insert(0, self.result)  # print self.result

    def create_widgets(self):
        self.create_stringvar()
        self.create_image()
        self.create_buttons()
        self.create_optionmenu()
        self.create_entry()

    def create_stringvar(self):
        self.unitevar1 = StringVar(self.window2)
        self.unitevar1.set(self.unite_of_measure[2])

        self.unitevar2 = StringVar(self.window2)
        self.unitevar2.set(self.unite_of_measure[2])

        self.unites = [self.unitevar1, self.unitevar2]

    def create_image(self):
        self.back_image = PhotoImage(file="img/transparent_back.png").subsample(3, 3)  # importing the back image (to MainApp)

    def create_buttons(self):
        self.back_button = Button(self.window2, image=self.back_image, bg="#303133", bd=0, highlightthicknes=0, activebackground="#262729", command=self.back)
        self.back_button.place(width=80, height=80)

        self.convert = Button(self.main_frame, text="Convert", font="Helvetica 15", bg="#303133", fg="#ECB613", command=self.convert)
        self.convert.grid(row=1, column=2, padx=(50, 50))

    def create_optionmenu(self):
        for index, frame in enumerate(self.frames):  # menu to select an unit of measure
            self.optionmenu = OptionMenu(frame, self.unites[index], *self.unite_of_measure)
            self.optionmenu.config(width=10, font="Helvetica 15", bg="#262729", fg="#ECB613", activebackground="#262729", activeforeground="#ECB613")
            self.optionmenu["menu"].config(bg="#262729", fg="#ECB613")
            self.optionmenu.pack(pady=(0, 50))

    def create_entry(self):
        self.entry1 = Entry(self.left_frame, bg="#262729", fg="#ECB613", font="Helvetica 20")
        self.entry1.pack()

        self.entry2 = Entry(self.right_frame, bg="#262729", fg="#ECB613", font="Helvetica 20")
        self.entry2.pack()
