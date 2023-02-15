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

        boxes = Frame(fram, width = 730, height = 600, bg = 'lightgrey')
        boxes.place(x=685, y = 700, anchor = S)


        self.letter1 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, anchor = N+W)
        self.letter2 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=120, anchor = N+W)
        self.letter3 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 240, anchor = N+W)
        self.letter4 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 360, anchor = N+W)
        self.letter5 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 480, anchor = N+W)
        self.letter6 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=600, anchor = N+W)

        self.letter7 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, anchor = N+W)
        self.letter8 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=120, y = 120, anchor = N+W)
        self.letter9 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 240, y = 240, anchor = N+W)
        self.letter10 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x = 360, y = 360, anchor = N+W)
        self.letter11 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x= 480, y = 480, anchor = N+W)
        self.letter12 = Text(boxes, width = 10, height = 5, wrap = WORD, font = ("Consolas", 15), bg = "#F8EDEB").place(in_= boxes, relx = .01, rely = .01, x=600, y = 600, anchor = N+W)
        """self.letter2 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter2.place(x = 5, y = 1, relx=0.01,  rely=0.01, anchor = N)
        self.letter3 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter3.place(x = 5, y = 2, relx=0.01,  rely=0.01, anchor = N)
        self.letter4 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter4.place(x = 5, y = 3, relx=0.01,  rely=0.01, anchor = N)

        self.letter5 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter5.place(x = 11, y = 0, relx=0.01,  rely=0.01, anchor = N)
        self.letter6 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter6.place(x = 11, y = 1, relx=0.01,  rely=0.01, anchor = N)
        self.letter7 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter7.place(x = 11, y = 2, relx=0.01,  rely=0.01, anchor = N)
        self.letter8 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter8.place(x = 11, y = 3, relx=0.01,  rely=0.01, anchor = N)

        self.letter9 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter9.place(x = 17, y = 0, relx=0.01,  rely=0.01, anchor = N)
        self.letter10 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter10.place(x = 17, y = 1, relx=0.01,  rely=0.01, anchor = N)
        self.letter11 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter11.place(x = 17, y = 2, relx=0.01,  rely=0.01, anchor = N)
        self.letter12 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter12.place(x = 17, y = 3, relx=0.01,  rely=0.01, anchor = N)

        self.letter13 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter13.place(x = 23, y = 0, relx=0.01,  rely=0.01, anchor = N)
        self.letter14 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter14.place(x = 23, y = 1, relx=0.01,  rely=0.01, anchor = N)
        self.letter15 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter15.place(x = 23, y = 2, relx=0.01,  rely=0.01, anchor = N)
        self.letter16 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter16.place(x = 23, y = 3, relx=0.01,  rely=0.01, anchor = N)

        self.letter17 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter17.place(x = 29, y = 0, relx=0.01,  rely=0.01, anchor = N)
        self.letter18 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter18.place(x = 29, y = 1, relx=0.01,  rely=0.01, anchor = N)
        self.letter19 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter19.place(x = 29, y = 2, relx=0.01,  rely=0.01, anchor = N)
        self.letter20 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter20.place(x = 29, y = 3, relx=0.01,  rely=0.01, anchor = N)

        self.letter21 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter21.place(x = 35, y = 0, relx=0.01,  rely=0.01, anchor = N)
        self.letter22 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter22.place(x = 35, y = 1, relx=0.01,  rely=0.01, anchor = N)
        self.letter23 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter23.place(x = 35, y = 2, relx=0.01,  rely=0.01, anchor = N)
        self.letter24 = Text(fram, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter24.place(x = 35, y = 3, relx=0.01,  rely=0.01, anchor = N)"""
        

    def retrieve_input(self):
        input = self.letter1w1.get("1.0",END)
        print(input)
    


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
        

        
    

