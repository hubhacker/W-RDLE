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
            self.letter1 = Text(self, width = 100, height = 10, wrap = WORD)
            self.letter1.grid(row = 3, column = 0, columnspan = 4)
            self.letter2 = Text(self, width = 100, height = 10, wrap = WORD)
            self.letter2.grid(row = 3, column = 1, columnspan = 4)
            self.letter3 = Text(self, width = 100, height = 10, wrap = WORD)
            self.letter3.grid(row = 3, column = 3, columnspan = 4)
            self.letter4 = Text(self, width = 100, height = 10, wrap = WORD)
            self.letter4.grid(row = 3, column = 3, columnspan = 4)
            self.letter5 = Text(self, width = 100, height = 10, wrap = WORD)
            self.letter5.grid(row = 3, column = 3, columnspan = 4)
            self.letter6 = Text(self, width = 100, height = 10, wrap = WORD)
            self.letter6.grid(row = 3, column = 3, columnspan = 4)

        # create entry box here
        Label(self, text = 'Guess: ').grid(row = 6, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 6, column = 1, sticky = W, columnspan=1)

        # create submit button
        Button(self, text= 'Submit!', fg='#FFFFFF', bg='#94add6', command = self.check_guess).grid(row = 7, column = 0, sticky = W)


    def check_guess(self):
        
        guess = self.guess_ent.get()
        ''
        while guess != self.hardword:
            pass

        letter = 
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)




    
        
        
        
    

