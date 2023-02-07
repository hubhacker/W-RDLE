from tkinter import *
import random

class Application(Frame):
    
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
        
        self.letter1w1 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter1w1.grid(row = 3, column = 0, columnspan = 4)
        self.letter2w1 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter2w1.grid(row = 3, column = 1, columnspan = 4)
        self.letter3w1 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter3w1.grid(row = 3, column = 2, columnspan = 4)
        self.letter4w1 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter4w1.grid(row = 3, column = 3, columnspan = 4)
        self.letter5w1 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter5w1.grid(row = 3, column = 4, columnspan = 4)
        self.letter6w1 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter6w1.grid(row = 3, column = 5, columnspan = 4)

        self.letter1w2 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter1w2.grid(row = 4, column = 0, columnspan = 4)
        self.letter2w2 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter2w2.grid(row = 4, column = 1, columnspan = 4)
        self.letter3w2 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter3w2.grid(row = 4, column = 2, columnspan = 4)
        self.letter4w2 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter4w2.grid(row = 4, column = 3, columnspan = 4)
        self.letter5w2 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter5w2.grid(row = 4, column = 4, columnspan = 4)
        self.letter6w2 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter6w2.grid(row = 4, column = 5, columnspan = 4)

        self.letter1w3 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter1w3.grid(row = 5, column = 0, columnspan = 4)
        self.letter2w3 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter2w3.grid(row = 5, column = 1, columnspan = 4)
        self.letter3w3 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter3w3.grid(row = 5, column = 2, columnspan = 4)
        self.letter4w3 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter4w3.grid(row = 5, column = 3, columnspan = 4)
        self.letter5w3 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter5w3.grid(row = 5, column = 4, columnspan = 4)
        self.letter6w3 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter6w3.grid(row = 5, column = 5, columnspan = 4)

        self.letter1w4 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter1w4.grid(row = 6, column = 0, columnspan = 4)
        self.letter2w4 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter2w4.grid(row = 6, column = 1, columnspan = 4)
        self.letter3w4 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter3w4.grid(row = 6, column = 2, columnspan = 4)
        self.letter4w4= Text(self, width = 10, height = 10, wrap = WORD)
        self.letter4w4.grid(row = 6, column = 3, columnspan = 4)
        self.letter5w4 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter5w4.grid(row = 6, column = 4, columnspan = 4)
        self.letter6w4 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter6w4.grid(row = 6, column = 5, columnspan = 4)

        self.letter1w5 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter1w5.grid(row = 3, column = 0, columnspan = 4)
        self.letter2w5 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter2w5.grid(row = 3, column = 1, columnspan = 4)
        self.letter3w5 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter3w5.grid(row = 3, column = 2, columnspan = 4)
        self.letter4w5 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter4w5.grid(row = 3, column = 3, columnspan = 4)
        self.letter5w5 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter5w5.grid(row = 3, column = 4, columnspan = 4)
        self.letter6w5 = Text(self, width = 10, height = 10, wrap = WORD)
        self.letter6w5.grid(row = 3, column = 5, columnspan = 4)



    def check_guess(self): # callback function
        
        guess = self.guess_ent.get()
        ''
        while guess != self.hardword:
            pass
        
        word_single = []
        for i in guess:
            word_single.append(i)
        letter = Label[i] = i
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)

    def show_msg(event):
        Label["text"]="Sale Up to 50% Off!"

    
win = Tk()
        
        
    

