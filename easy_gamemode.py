from tkinter import *
import random

class Easy(Frame):

    def __init__(self,master):

        super(Easy, self).__init__(master)
        self.create_widgets()
        self.file=("midyear_4letterwords.txt")
    
    def choose_word(self,file):

        fourletter = open(file)

        self.fourletterList = []

        for word in fourletter:
            self.fourletterList.append(word.strip())

        self.easyword = self.fourletterList([random.randint(0, 1000)])
    
    def create_widgets(self):
        
        root.title("Easy Mode")
        root.geometry("400x600")
        root.maxsize(400, 600)
        root.config(bg = "#F8EDEB")

        self.frame = Frame(root, width = 300, height = 400, bg = "#F9DCC4")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)

        Label(self.frame, text = "EASY MODE", font=("Consolas", 13), bg = "#F9DCC4").place(relx = 0.5, rely = 0.05, anchor = N)

        

        self.letter1 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter1.place(x = 5, y = 1, anchor = N)
        self.letter2 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter2.place(x = 5, y = 1, anchor = N)
        self.letter3 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter3.place(x = 5, y = 2, anchor = N)
        self.letter4 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter4.place(x = 5, y = 3, anchor = N)

        self.letter5 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter5.place(relx = 11, y = 0, anchor = N)
        self.letter6 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter6.place(x = 11, y = 1, anchor = N)
        self.letter7 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter7.place(x = 11, y = 2, anchor = N)
        self.letter8 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter8.place(x = 11, y = 3, anchor = N)

        self.letter9 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter9.place(x = 17, y = 0, anchor = N)
        self.letter10 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter10.place(x = 17, y = 1, anchor = N)
        self.letter11 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter11.place(x = 17, y = 2, anchor = N)
        self.letter12 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter12.place(x = 17, y = 3, anchor = N)

        self.letter13 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter13.place(x = 23, y = 0, anchor = N)
        self.letter14 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter14.place(x = 23, y = 1, anchor = N)
        self.letter15 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter15.place(x = 23, y = 2, anchor = N)
        self.letter16 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter16.place(x = 23, y = 3, anchor = N)

        self.letter17 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter17.place(x = 29, y = 0, anchor = N)
        self.letter18 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter18.place(x = 29, y = 1, anchor = N)
        self.letter19 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter19.place(x = 29, y = 2, anchor = N)
        self.letter20 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter20.place(x = 29, y = 3, anchor = N)

        self.letter21 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter21.place(x = 35, y = 0, anchor = N)
        self.letter22 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter22.place(x = 35, y = 1, anchor = N)
        self.letter23 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter23.place(x = 35, y = 2, anchor = N)
        self.letter24 = Text(root, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter24.place(x = 35, y = 3, anchor = N)
        
    def check_guess(self): # callback function
        
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
root.title("Easy Mode")
app = Easy(root)
root.mainloop()