from tkinter import *
import random

class Application (Frame):

    def __init__(self, file, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.file = file
        file = ("midyear_5letterwords.txt")

    def choose_word(self, file): 

        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.intword = self.fiveletterlist([random.randint(0, 1000)])

    
    def create_widgets(self):

        Label(self, text= "INTERMEDIATE MODE").grid(row = 0, column= 1, columnspan= 1, sticky = W+E)
        self.letter1 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter1.grid(row = 8, column = 0, columnspan = 4)
        self.letter2 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter2.grid(row = 8, column = 1, columnspan = 4)
        self.letter3 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter3.grid(row = 8, column = 2, columnspan = 4)
        self.letter4 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter4.grid(row = 8, column = 3, columnspan = 4)
        self.letter5 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter5.grid(row = 8, column = 4, columnspan = 4)


    def guess_check(self):

        guess = 