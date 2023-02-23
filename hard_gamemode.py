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
        fram  =  Frame(root,  width=1370,  height=1500,  bg='grey')
        fram.place(x=0,  y=0,  relx=0,  rely=0)

        Label(fram, text = "HARD MODE", font=("Consolas", 50)).place(x=685, y= 50, anchor = CENTER)

        boxes = Frame(fram, width = 730, height = 615, bg = 'lightgrey')
        boxes.place(x=685, y = 700, anchor = S)


        self.letter1 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, anchor = N+W)
        self.letter2 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=120, anchor = N+W)
        self.letter3 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 240, anchor = N+W)
        self.letter4 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 360, anchor = N+W)
        self.letter5 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 480, anchor = N+W)
        self.letter6 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=600, anchor = N+W)

        self.letter7 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 0, y= 130, anchor = N+W)
        self.letter8 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=120, y = 130, anchor = N+W)
        self.letter9 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 240, y = 130, anchor = N+W)
        self.letter10 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 360, y = 130, anchor = N+W)
        self.letter11 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 480, y = 130, anchor = N+W)
        self.letter12 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=600, y = 130, anchor = N+W)
       
        self.letter7 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 0, y= 260, anchor = N+W)
        self.letter8 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=120, y = 260, anchor = N+W)
        self.letter9 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 240, y = 260, anchor = N+W)
        self.letter10 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 360, y = 260, anchor = N+W)
        self.letter11 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 480, y = 260, anchor = N+W)
        self.letter12 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=600, y = 260, anchor = N+W)

        self.letter7 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 0, y= 390, anchor = N+W)
        self.letter8 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=120, y = 390, anchor = N+W)
        self.letter9 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 240, y = 390, anchor = N+W)
        self.letter10 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 360, y = 390, anchor = N+W)
        self.letter11 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 480, y = 390, anchor = N+W)
        self.letter12 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=600, y = 390, anchor = N+W)
       
        self.letter7 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 0, y= 520, anchor = N+W)
        self.letter8 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=120, y = 520, anchor = N+W)
        self.letter9 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 240, y = 520, anchor = N+W)
        self.letter10 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 360, y = 520, anchor = N+W)
        self.letter11 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 480, y = 520, anchor = N+W)
        self.letter12 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=600, y = 520, anchor = N+W)

    def retrieve_input(self):
        input = self.letter1.get("1.0",END)
        return input
    
    


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
root.title("Hard")
app = Hard(root)
root.mainloop()
        

        
    

