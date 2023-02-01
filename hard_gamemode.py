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

        # create label boxes here

        Label()
        
        self.letter1 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter1.grid(row = 8, column = 0, columnspan = 4)
        self.letter2 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter2.grid(row = 8, column = 0, columnspan = 4)
        self.letter3 = Text(self, width = 100, height = 10, wrap = WORD)
        self.letter3.grid(row = 8, column = 0, columnspan = 4)

        

    def check_guess(self):
        
        guess = self.guess_ent.get()
        
        while guess != self.hardword:


        
        
        self..delete(0.0, END)
        self.story_txt.insert(0.0, story)




    
        
        
        
    

