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


        left_frame  =  Frame(root,  width=250,  height=500,  bg='grey')
        left_frame.place(x=10,  y=10,  relx=0.01,  rely=0.01)

        Label(left_frame, text = "Hard MODE", font=("Consolas", 13)).place(relx = 0, anchor = N)

        self.letter1 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter1.place(relx = 5, rely = 1, anchor = N)
        self.letter2 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter2.place(relx = 5, rely = 1, anchor = N)
        self.letter3 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter3.place(relx = 5, rely = 2, anchor = N)
        self.letter4 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter4.place(relx = 5, rely = 3, anchor = N)

        self.letter5 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter5.place(relx = 50, rely = 0, anchor = N)
        self.letter6 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter6.place(relx = 50, rely = 1, anchor = N)
        self.letter7 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter7.place(relx = 11, rely = 2, anchor = N)
        self.letter8 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter8.place(relx = 11, rely = 3, anchor = N)

        self.letter9 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter9.place(relx = 17, rely = 0, anchor = N)
        self.letter10 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter10.place(relx = 17, rely = 1, anchor = N)
        self.letter11 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter11.place(relx = 17, rely = 2, anchor = N)
        self.letter12 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter12.place(relx = 17, rely = 3, anchor = N)

        self.letter13 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter13.place(relx = 23, rely = 0, anchor = N)
        self.letter14 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter14.place(relx = 23, rely = 1, anchor = N)
        self.letter15 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter15.place(relx = 23, rely = 2, anchor = N)
        self.letter16 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter16.place(relx = 23, rely = 3, anchor = N)

        self.letter17 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter17.place(relx = 29, rely = 0, anchor = N)
        self.letter18 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter18.place(relx = 29, rely = 1, anchor = N)
        self.letter19 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter19.place(relx = 29, rely = 2, anchor = N)
        self.letter20 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter20.place(relx = 29, rely = 3, anchor = N)

        self.letter21 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter21.place(relx = 35, rely = 0, anchor = N)
        self.letter22 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter22.place(relx = 35, rely = 1, anchor = N)
        self.letter23 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter23.place(relx = 35, rely = 2, anchor = N)
        self.letter24 = Text(left_frame, width = 10, height = 5, wrap = WORD, font = ("Consolas"), bg = "#F8EDEB")
        self.letter24.place(relx = 35, rely = 3, anchor = N)
        

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
        

        
    

