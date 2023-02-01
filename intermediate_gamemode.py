from tkinter import *
import random

class Application (Frame):

    def __init__(self, file, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.file = file
        file = open("midyear_5letterwords.txt")

    def choose_word(self, file): 
        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.word = self.fiveletterlist([random.randint(0, 1000)])

    
    def create_widgets(self):

        # create label boxes here

        Label()
        self.letter1 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter1.grid(row = 8, column = 0, columnspan = 4)
        self.letter2 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter2.grid(row = 8, column = 0, columnspan = 4)
        self.letter3 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter3.grid(row = 8, column = 0, columnspan = 4)
        self.letter4 = Text(self, )
        self.letter4.grid()
        self.letter5 = Text(self, )
        self.letter5.grid()

