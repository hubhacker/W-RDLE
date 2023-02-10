from tkinter import *
import random

class Hard(Frame):
    
    def __init__(self, master):
        super(Hard, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.file = "midyear_6letterwords.txt"

    def choose_word(self): 
        sixletter = open("midyear_6letterwords.txt")

        self.sixletterlist = []

        for word in sixletter:
            self.sixletterlist.append(word.strip())

        self.hardword = self.sixletterlist([random.randint(0, 1000)])

    def create_widgets(self):
        # create label boxes here
        Label(self, text="HARD MODE", font=("Helvetica", 20), width=20).grid(row=0, column=1, columnspan=4, sticky=N)

        self.letter1w1 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter1w1.grid(row = 3, column = 0, columnspan = 1)
        self.letter2w1 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter2w1.grid(row = 3, column = 1, columnspan = 1)
        self.letter3w1 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter3w1.grid(row = 3, column = 2, columnspan = 1)
        self.letter4w1 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter4w1.grid(row = 3, column = 3, columnspan = 1)
        self.letter5w1 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter5w1.grid(row = 3, column = 4, columnspan = 1)
        self.letter6w1 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter6w1.grid(row = 3, column = 5, columnspan = 1)

        self.letter1w2 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter1w2.grid(row = 4, column = 0, columnspan = 1)
        self.letter2w2 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter2w2.grid(row = 4, column = 1, columnspan = 1)
        self.letter3w2 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter3w2.grid(row = 4, column = 2, columnspan = 1)
        self.letter4w2 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter4w2.grid(row = 4, column = 3, columnspan = 1)
        self.letter5w2 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter5w2.grid(row = 4, column = 4, columnspan = 1)
        self.letter6w2 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter6w2.grid(row = 4, column = 5, columnspan = 1)

        self.letter1w3 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter1w3.grid(row = 5, column = 0, columnspan = 1)
        self.letter2w3 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter2w3.grid(row = 5, column = 1, columnspan = 1)
        self.letter3w3 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter3w3.grid(row = 5, column = 2, columnspan = 1)
        self.letter4w3 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter4w3.grid(row = 5, column = 3, columnspan = 1)
        self.letter5w3 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter5w3.grid(row = 5, column = 4, columnspan = 1)
        self.letter6w3 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter6w3.grid(row = 5, column = 5, columnspan = 1)

        self.letter1w4 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter1w4.grid(row = 6, column = 0, columnspan = 1)
        self.letter2w4 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter2w4.grid(row = 6, column = 1, columnspan = 1)
        self.letter3w4 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter3w4.grid(row = 6, column = 2, columnspan = 1)
        self.letter4w4= Text(self, height = 5, width = 10, wrap = WORD)
        self.letter4w4.grid(row = 6, column = 3, columnspan = 1)
        self.letter5w4 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter5w4.grid(row = 6, column = 4, columnspan = 1)
        self.letter6w4 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter6w4.grid(row = 6, column = 5, columnspan = 1)

        self.letter1w5 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter1w5.grid(row = 3, column = 0, columnspan = 1)
        self.letter2w5 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter2w5.grid(row = 3, column = 1, columnspan = 1)
        self.letter3w5 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter3w5.grid(row = 3, column = 2, columnspan = 1)
        self.letter4w5 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter4w5.grid(row = 3, column = 3, columnspan = 1)
        self.letter5w5 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter5w5.grid(row = 3, column = 4, columnspan = 1)
        self.letter6w5 = Text(self, height = 5, width = 10, wrap = WORD)
        self.letter6w5.grid(row = 3, column = 5, columnspan = 1)

        self.letter1w1 = Entry(self)
        self.letter1w1.grid(row = 20, column = 0, columnspan = 1)

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

    
root = Tk()
root.title("Hard")
app = Hard(root)
root.mainloop()
        

        
    

