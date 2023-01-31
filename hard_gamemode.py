from tkinter import *
import random

class Grid:
    
    def create_widgets(self):
        Label(self, text = 'Guess!:', font = 'Helvetica 15 bold', fg = "navy blue").grid(row = 'pass')
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 'pass')

class Word:
    
    def __init__(self, hardword):
        self.hardword = hardword
        
    def choose_word(self, file): 
        sixletter = open(file)

        self.sixletterlist = []

        for word in sixletter:
            self.sixletterlist.append(word.strip())

        self.hardword = self.sixletterlist([random.randint(0, 1000)])

class Guess:
    

    guessed = False

    while guessed == False:
        
        
    

