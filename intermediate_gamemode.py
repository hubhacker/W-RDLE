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

        Label(self.frame, text = "INTERMEDIATE MODE", font=("Consolas", 13)).place(relx = 0.5, rely = 0.05, anchor = N)

        self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter1.place(x = 1, rely = 0, columnspan = 1)
        self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter2.place(relx = 5, rely = 1, columnspan = 1)
        self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter3.place(relx = 5, rely = 2, columnspan = 1)
        self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter4.place(relx = 5, rely = 3, columnspan = 1)
        self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter5.place(relx = 5, rely = 4, columnspan = 1)

        self.letter6 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter6.place(relx = 11, rely = 0, columnspan = 1)
        self.letter7 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter7.place(relx = 11, rely = 1, columnspan = 1)
        self.letter8 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter8.place(relx = 11, rely = 2, columnspan = 1)
        self.letter9 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter9.place(relx = 11, rely = 3, columnspan = 1)
        self.letter10 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter10.place(relx = 11, rely = 4, columnspan = 1)

        self.letter11 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter11.place(relx = 17, rely = 0, columnspan = 1)
        self.letter12 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter12.place(relx = 17, rely = 1, columnspan = 1)
        self.letter13 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter13.place(relx = 17, rely = 2, columnspan = 1)
        self.letter14 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter14.place(relx = 17, rely = 3, columnspan = 1)
        self.letter15 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter15.place(relx = 17, rely = 4, columnspan = 1)

        self.letter16 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter16.place(relx = 23, rely = 0, columnspan = 1)
        self.letter17 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter17.place(relx = 23, rely = 1, columnspan = 1)
        self.letter18 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter18.place(relx = 23, rely = 2, columnspan = 1)
        self.letter19 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter19.place(relx = 23, rely = 3, columnspan = 1)
        self.letter20 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter20.place(relx = 23, rely = 4, columnspan = 1)

        self.letter21 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter21.place(relx = 29, rely = 0, columnspan = 1)
        self.letter22 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter22.place(relx = 29, rely = 1, columnspan = 1)
        self.letter23 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter23.place(relx = 29, rely = 2, columnspan = 1)
        self.letter24 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter24.place(relx = 29, rely = 3, columnspan = 1)
        self.letter25 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"))
        self.letter25.place(relx = 29, rely = 4, columnspan = 1)
        
       
        
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