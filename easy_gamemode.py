from tkinter import *
import random

class Easy(Frame):

    def __init__(self,master):

        super(Easy, self).__init__(master)
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

        Label(self, text = "EASY MODE").grid(row=0, column=1, sticky=N)

        self.letter1 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Ariel"), bg = "#F8EDEB")
        self.letter1.grid(row = 5, column = 0, columnspan = 1)
        self.letter2 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter2.grid(row = 5, column = 1, columnspan = 1)
        self.letter3 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter3.grid(row = 5, column = 2, columnspan = 1)
        self.letter4 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter4.grid(row = 5, column = 3, columnspan = 1)

        self.letter5 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter5.grid(row = 11, column = 0, columnspan = 1)
        self.letter6 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter6.grid(row = 11, column = 1, columnspan = 1)
        self.letter7 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter7.grid(row = 11, column = 2, columnspan = 1)
        self.letter8 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter8.grid(row = 11, column = 3, columnspan = 1)

        self.letter9 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter9.grid(row = 17, column = 0, columnspan = 1)
        self.letter10 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter10.grid(row = 17, column = 1, columnspan = 1)
        self.letter11 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter11.grid(row = 17, column = 2, columnspan = 1)
        self.letter12 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter12.grid(row = 17, column = 3, columnspan = 1)

        self.letter13 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter13.grid(row = 23, column = 0, columnspan = 1)
        self.letter14 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter14.grid(row = 23, column = 1, columnspan = 1)
        self.letter15 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter15.grid(row = 23, column = 2, columnspan = 1)
        self.letter16 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter16.grid(row = 23, column = 3, columnspan = 1)

        self.letter17 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter17.grid(row = 29, column = 0, columnspan = 1)
        self.letter18 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter18.grid(row = 29, column = 1, columnspan = 1)
        self.letter19 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter19.grid(row = 29, column = 2, columnspan = 1)
        self.letter20 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter20.grid(row = 29, column = 3, columnspan = 1)

        self.letter21 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter21.grid(row = 35, column = 0, columnspan = 1)
        self.letter22 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter22.grid(row = 35, column = 1, columnspan = 1)
        self.letter23 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter23.grid(row = 35, column = 2, columnspan = 1)
        self.letter24 = Text(self, width = 10, height = 5, wrap = WORD)
        self.letter24.grid(row = 35, column = 3, columnspan = 1)
        
    def check_guess(self):
        
        guess = self.guess_ent.get()
        
        while guess != self.easyword:
            pass
        
        word_single = []
        for i in guess:
            word_single.append(i)
        letter = Label[i] = i
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)

root = Tk()
root.title("Easy")
app = Easy(root)
root.mainloop()