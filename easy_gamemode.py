from tkinter import *
import random

class Grid(Frame):

    def __init__(self,master,file):

        super(self).__init__(master)
        self.grid()
        self.create_widgets()
        self.file=file
        file=("midyear_4letterwords.txt")
    
    def choose_word(self,file):

        fourletter = open(file)

        self.fourletterList = []

        for word in fourletter:
            self.fourletterList.append(word.strip())

        self.easyword = self.fourletterList([random.randint(0, 1000)])
    
    def create_widgets(self):

        Label(text="EASY MODE")
        
        self.letter1 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter1.grid(row = 8, column = 0, columnspan = 4)
        self.letter2 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter2.grid(row = 8, column = 0, columnspan = 4)
        self.letter3 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter3.grid(row = 8, column = 0, columnspan = 4)