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
