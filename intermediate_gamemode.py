from tkinter import *
import random

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

        root.title("Intermediate Mode")
        root.geometry("400x600")
        root.maxsize(400, 600)
        root.config(bg = "")

        self.frame = Frame(root, width = 300, height = 400, bg = "#F9DCC4")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)

        Label(self, text= "INTERMEDIATE MODE").place(x = 0, column= 1, columnspan= 1, sticky = W+E)

        self.letter1 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter1.place(x= 1, y = 0, columnspan = 1)

        self.letter2 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter2.place(x = 5, y= 1, columnspan = 1)

        self.letter3 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter3.place(x = 5, y= 2, columnspan = 1)

        self.letter4 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter4.place(x = 5, y= 3, columnspan = 1)

        self.letter5 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter5.place(x = 5, y= 4, columnspan = 1)


        self.letter6 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter6.place(x = 11, y= 0, columnspan = 1)

        self.letter7 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter7.place(x = 11, y= 1, columnspan = 1)

        self.letter8 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter8.place(x = 11, y= 2, columnspan = 1)

        self.letter9 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter9.place(x = 11, y= 3, columnspan = 1)

        self.letter10 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter10.place(x = 11, y= 4, columnspan = 1)


        self.letter11 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter11.place(x = 17, y= 0, columnspan = 1)

        self.letter12 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter12.place(x = 17, y= 1, columnspan = 1)

        self.letter13 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter13.place(x = 17, y= 2, columnspan = 1)

        self.letter14 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter14.place(x = 17, y= 3, columnspan = 1)

        self.letter15 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter15.place(x = 17, y= 4, columnspan = 1)

        self.letter16 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter16.place(x = 23, y= 0, columnspan = 1)
        
        self.letter17 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter17.place(x = 23, y= 1, columnspan = 1)

        self.letter18 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter18.place(x = 23, y= 2, columnspan = 1)

        self.letter19 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter19.place(x = 23, y= 3, columnspan = 1)

        self.letter20 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter20.place(x = 23, y= 4, columnspan = 1)

        self.letter21 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter21.place(x = 29, y= 0, columnspan = 1)

        self.letter22 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter22.place(x = 29, y= 1, columnspan = 1)

        self.letter23 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter23.place(x = 29, y= 2, columnspan = 1)
        
        self.letter24 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter24.place(x = 29, y= 3, columnspan = 1)

        self.letter25 = Text(self, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#CDB4DB")
        self.letter25.place(x = 29, y= 4, columnspan = 1)
        
       
        
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