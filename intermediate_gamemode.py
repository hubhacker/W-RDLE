from tkinter import *
import random

class Intermediate(Frame):

    def __init__(self, master):

        super(Intermediate, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.file = ("midyear_5letterwords.txt")

    def choose_word(self, file): 

        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.intword = self.fiveletterlist([random.randint(0, 1000)])

    
    def create_widgets(self):

        Label(self, text= "INTERMEDIATE MODE").grid(row = 0, column= 1, columnspan= 1, sticky = W+E)

        self.letter1 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter1.grid(row = 5, column = 0, columnspan = 1)
        self.letter2 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter2.grid(row = 5, column = 1, columnspan = 1)
        self.letter3 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter3.grid(row = 5, column = 2, columnspan = 1)
        self.letter4 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter4.grid(row = 5, column = 3, columnspan = 1)
        self.letter5 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter5.grid(row = 5, column = 4, columnspan = 1)


        
        

        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 6, column = 1, sticky = W, columnspan=1)
        
       
        
    def check_guess(self): # callback function
        
        guess = self.guess_ent.get()
        
        while guess != self.intword:
            pass
        
        word_single = []
        for i in guess:
            word_single.append(i)
        letter = Label[i] = i
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)

root = Tk() 
root.title("Intermediate Mode")
app = Intermediate(root)
root.mainloop()