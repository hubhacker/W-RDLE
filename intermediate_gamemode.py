from tkinter import *
import random

class Intermediate(Frame):

    def __init__(self, master):

        super(Intermediate, self).__init__(master)
        #self.place()
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
        root.config(bg = "#F8EDEB") # I'LL CHANGE BG LATER

        self.frame = Frame(root, width = 300, height = 400, bg = "#F9DCC4") # I'LL CHANGE BG LATER
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)

        Label(self.frame, text = "INTERMEDIATE MODE", font=("Consolas", 13), bg = "#F9DCC4").place(relx = 0.5, rely = 0.05, anchor = N) # vivian i will change the color later, i can't rn bc i have no wifi

        self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter1.place(relx = 0.2, rely = 0.14, anchor = N)
        self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter2.place(relx = 0.4, rely = 0.14, anchor = N)
        self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter3.place(relx = 0.6, rely = 0.14, anchor = N)
        self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter4.place(relx = 0.8, rely = 0.14, anchor = N)
        self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter5.place(relx = 1, rely = 0.14, anchor = N)

        self.letter6 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter6.place(relx = 0.2, rely = 0.28, anchor = N)
        self.letter7 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter7.place(relx = 0.4, rely = 0.28, anchor = N)
        self.letter8 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter8.place(relx = 0.6, rely = 0.28, anchor = N)
        self.letter9 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter9.place(relx = 0.8, rely = 0.28, anchor = N)
        self.letter10 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter10.place(relx = 1, rely = 0.28, anchor = N)

        self.letter11 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter11.place(relx = 0.2, rely = 0.41, anchor = N)
        self.letter12 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter12.place(relx = 0.4, rely = 0.41, anchor = N)
        self.letter13 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter13.place(relx = 0.6, rely = 0.41, anchor = N)
        self.letter14 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter14.place(relx = 0.8, rely = 0.41, anchor = N)
        self.letter15 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter15.place(relx = 1, rely = 0.41, anchor = N)

        self.letter16 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter16.place(relx = 0.2, rely = 0.54, anchor = N)
        self.letter17 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter17.place(relx = 0.4, rely = 0.54, anchor = N)
        self.letter18 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter18.place(relx = 0.6, rely = 0.54, anchor = N)
        self.letter19 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter19.place(relx = 0.8, rely = 0.54, anchor = N)
        self.letter20 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter20.place(relx = 1, rely = 0.54, anchor = N)

        self.letter21 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter21.place(relx = 0.2, rely = 0.67, anchor = N)
        self.letter22 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter22.place(relx = 0.4, rely = 0.67, anchor = N)
        self.letter23 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter23.place(relx = 0.6, rely = 0.67, anchor = N)
        self.letter24 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter24.place(relx = 0.8, rely = 0.67, anchor = N)
        self.letter25 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
        self.letter25.place(relx = 1, rely = 0.67, anchor = N)
        
    def guess_ent(self):
        pass
        
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