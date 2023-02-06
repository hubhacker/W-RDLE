from tkinter import *
import random

class Grid(Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def choose_word(self, file): 
        sixletter = open(file)

        self.sixletterlist = []

        for word in sixletter:
            self.sixletterlist.append(word.strip())

        self.hardword = self.sixletterlist([random.randint(0, 1000)])

    def create_widgets(self):
        x = 6
        # create label boxes here
        
        for i in range(x):
            self.letter1 = Text(self, width = 10, height = 10, wrap = WORD)
            self.letter1.grid(row = 3, column = 0, columnspan = 4)
            self.letter2 = Text(self, width = 10, height = 10, wrap = WORD)
            self.letter2.grid(row = 3, column = 1, columnspan = 4)
            self.letter3 = Text(self, width = 10, height = 10, wrap = WORD)
            self.letter3.grid(row = 3, column = 2, columnspan = 4)
            self.letter4 = Text(self, width = 10, height = 10, wrap = WORD)
            self.letter4.grid(row = 3, column = 3, columnspan = 4)
            self.letter5 = Text(self, width = 10, height = 10, wrap = WORD)
            self.letter5.grid(row = 3, column = 4, columnspan = 4)
            self.letter6 = Text(self, width = 10, height = 10, wrap = WORD)
            self.letter6.grid(row = 3, column = 5, columnspan = 4)

        # enter trigger
        # create submit button
        
        win.bind('<Return>', variable = self.check_guess)

    def check_guess(event, self):
        
        guess = self.guess_ent.get()
        ''
        while guess != self.hardword:
            pass
        
        word_single = []
        for i in guess:
            word_single.append(i)
        letter = Label[i] = 'i'
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)




    
win = Tk()
        
        
    

