from tkinter import *
import random

class Easy(Frame):

    def __init__(self,master):

        super(self).__init__(master)
        self.grid()
        self.create_widgets()
        self.file=("midyear_4letterwords.txt")
    
    def choose_word(self,file):

        fourletter = open(file)

        self.fourletterList = []

        for word in fourletter:
            self.fourletterList.append(word.strip())

        self.easyword = self.fourletterList([random.randint(0, 1000)])
    
    def create_widgets(self):

        Label(self, text = "EASY MODE").grid(row=0, column=1, columnspan = 1, sticky=N)

        self.letter1 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter1.grid(row = 8, column = 0, columnspan = 4)
        self.letter2 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter2.grid(row = 8, column = 0, columnspan = 4)
        self.letter3 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter3.grid(row = 8, column = 0, columnspan = 4)
        self.letter4 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter4.grid(row = 3, column = 3, columnspan = 4)
    
        Label(self, text = 'Guess: ').grid(row = 6, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 6, column = 1, sticky = W, columnspan=1)
        
        # create submit button
        Button(self, text= 'Submit!', fg='#FFFFFF', bg='#94add6', command = self.check_guess).grid(row = 7, column = 0, sticky = W)
        
    def check_guess(self): # callback function
        
        guess = self.guess_ent.get()
        
        while guess != self.easyword:
            pass
        
        word_single = []
        for i in guess:
            word_single.append(i)
        letter = Label[i] = i
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)