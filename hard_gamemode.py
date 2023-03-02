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
        root.title("HARD MODE")
        root.geometry("400x600")
        root.maxsize(400, 600)
        root.config(bg = "#F8EDEB")

        self.frame = Frame(root, width = 300, height = 500, bg = "#4f7aa8")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)

        Label(self.frame, text = "HARD MODE", font=("Consolas", 13), bg = "#4f7aa8").place(relx = 0.5, rely = 0.05, anchor = N)

        rel_x = .1
        rel_y = .14

        #self.testletter = Entry(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        #self.testletter.place(relx = 1, rely = .84, anchor = N)

        self.test_ent = Entry(self.frame)
        self.test_ent.place(relx = 1, rely = .84, anchor = N)
        for i in range(0, 6):
            self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#c3d1e0")
            self.letter1.place(relx = rel_x, rely = rel_y, anchor = N)
            self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#c3d1e0")
            self.letter2.place(relx = rel_x + 0.15, rely = rel_y, anchor = N)
            self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#c3d1e0")
            self.letter3.place(relx = rel_x +.3, rely = rel_y, anchor = N)
            self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#c3d1e0")
            self.letter4.place(relx = rel_x+.45, rely = rel_y, anchor = N)
            self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#c3d1e0")
            self.letter5.place(relx = rel_x+.6, rely = rel_y, anchor = N)
            self.letter6 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#c3d1e0")
            self.letter6.place(relx = rel_x+.75, rely = rel_y, anchor = N)
            
            rel_y += .14
    def retrieve_word1(self, event):

        l1 = self.letter1.get(1.0, "end-1c")
        l2 = self.letter2.get(1.0, "end-1c")
        l3 = self.letter3.get(1.0, "end-1c")
        l4 = self.letter4.get(1.0, "end-1c")
        l5 = self.letter5.get(1.0, "end-1c")
        l6 = self.letter6.get(1.0, "end-1c")

        word = l1 + l2 + l3 + l4 + l5 + l6
        return word



        

        
    


    # def check_guess(self): # callback function
        
        """testing = self.letter1w1.get()
        self.test.delete(0.0, END)
        self.test.insert(0.0, testing+'omg')"""
        
        """while guess != self.hardword:
            pass
        
        word_single = []
        for i in guess:
            word_single.append(i)
        letter = Label[i] = i
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)"""
    
root = Tk()

root.bind('<Return>, retrieve_word1')

root.title("Hard")
app = Hard(root)
root.mainloop()
        

        
    

