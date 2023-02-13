from tkinter import *
import random
import tkinter.messagebox

class Intermediate(Frame):

    def __init__(self, master):

        super(Intermediate, self).__init__(master)
        self.place()
        self.create_widgets()
        self.file = ("midyear_5letterwords.txt")

    def choose_word(self, file): 

        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.intword = self.fiveletterlist([random.randint(0, 1000)])

    
    def create_widgets(self):

        Label(self, text= "INTERMEDIATE MODE").place(row = 0, column= 1, columnspan= 1, sticky = W+E)

        self.letter1 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter1.place(relx = 1, rely= = 0, columnspan = 1)

        self.letter2 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter2.place(row = 5, column = 1, columnspan = 1)

        self.letter3 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter3.place(row = 5, column = 2, columnspan = 1)

        self.letter4 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter4.place(row = 5, column = 3, columnspan = 1)

        self.letter5 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter5.place(row = 5, column = 4, columnspan = 1)


        self.letter6 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter6.place(row = 11, column = 0, columnspan = 1)

        self.letter7 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter7.place(row = 11, column = 1, columnspan = 1)

        self.letter8 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter8.place(row = 11, column = 2, columnspan = 1)

        self.letter9 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter9.place(row = 11, column = 3, columnspan = 1)

        self.letter10 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter10.place(row = 11, column = 4, columnspan = 1)


        self.letter11 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter11.place(row = 17, column = 0, columnspan = 1)

        self.letter12 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter12.place(row = 17, column = 1, columnspan = 1)

        self.letter13 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter13.place(row = 17, column = 2, columnspan = 1)

        self.letter14 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter14.place(row = 17, column = 3, columnspan = 1)

        self.letter15 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter15.place(row = 17, column = 4, columnspan = 1)

        self.letter16 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter16.place(row = 23, column = 0, columnspan = 1)
        
        self.letter17 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter17.place(row = 23, column = 1, columnspan = 1)

        self.letter18 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter18.place(row = 23, column = 2, columnspan = 1)

        self.letter19 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter19.place(row = 23, column = 3, columnspan = 1)

        self.letter20 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter20.place(row = 23, column = 4, columnspan = 1)

        self.letter21 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter21.place(row = 29, column = 0, columnspan = 1)

        self.letter22 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter22.place(row = 29, column = 1, columnspan = 1)

        self.letter23 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter23.place(row = 29, column = 2, columnspan = 1)
        
        self.letter24 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter24.place(row = 29, column = 3, columnspan = 1)

        self.letter25 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter25.place(row = 29, column = 4, columnspan = 1)
        
       
        
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