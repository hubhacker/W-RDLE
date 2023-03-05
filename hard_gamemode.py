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
        canvas = Canvas()
        root.geometry("400x600")
        root.maxsize(400, 600)
        root.config(bg = "#FFE8D6")

        self.button_bg = Button(root, width = 400, height = 600, bg = '#32a852').place(x= 0, y = 0, relx = 0, rely= 0)

        self.frame = Frame(root, width = 300, height = 500, bg = "#CB997E")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)
        
        

        Label(self.frame, text = "HARD MODE", font=("Consolas", 13), bg = "#CB997E").place(relx = 0.5, rely = 0.05, anchor = N)

        rel_x = .1
        rel_y = .14

        #Button(self., text = " test ", command = self.retrieve_word1, font =("Consolas", 15), fg = "black", bg = "#F9DCC4", width=13, height=1).place(relx = .85, rely = .90, anchor = N)
        
        self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter1.place(relx = rel_x, rely = rel_y, anchor = N)
        self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter2.place(relx = rel_x + 0.15, rely = rel_y, anchor = N)
        self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter3.place(relx = rel_x +.3, rely = rel_y, anchor = N)
        self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter4.place(relx = rel_x+.45, rely = rel_y, anchor = N)
        self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter5.place(relx = rel_x+.6, rely = rel_y, anchor = N)
        self.letter6 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter6.place(relx = rel_x+.75, rely = rel_y, anchor = N)
        
        self.letter7 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter7.place(relx = rel_x, rely = rel_y+.14, anchor = N)
        self.letter8 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter8.place(relx = rel_x + 0.15, rely = rel_y+.14, anchor = N)
        self.letter9 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter9.place(relx = rel_x +.3, rely = rel_y+.14, anchor = N)
        self.letter10 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter10.place(relx = rel_x+.45, rely = rel_y+.14, anchor = N)
        self.letter11 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter11.place(relx = rel_x+.6, rely = rel_y+.14, anchor = N)
        self.letter12 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter12.place(relx = rel_x+.75, rely = rel_y+.14, anchor = N)

        self.letter13 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter13.place(relx = rel_x, rely = rel_y+.28, anchor = N)
        self.letter14 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter14.place(relx = rel_x + 0.15, rely = rel_y+.28, anchor = N)
        self.letter15 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter15.place(relx = rel_x +.3, rely = rel_y+.28, anchor = N)
        self.letter16 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter16.place(relx = rel_x+.45, rely = rel_y+.28, anchor = N)
        self.letter17 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter17.place(relx = rel_x+.6, rely = rel_y+.28, anchor = N)
        self.letter18 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter18.place(relx = rel_x+.75, rely = rel_y+.28, anchor = N)

        self.letter19 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter19.place(relx = rel_x, rely = rel_y+.42, anchor = N)
        self.letter20 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter20.place(relx = rel_x + 0.15, rely = rel_y+.42, anchor = N)
        self.letter21 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter21.place(relx = rel_x +.3, rely = rel_y+.42, anchor = N)
        self.letter22 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter22.place(relx = rel_x+.45, rely = rel_y+.42, anchor = N)
        self.letter23 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter23.place(relx = rel_x+.6, rely = rel_y+.42, anchor = N)
        self.letter24 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter24.place(relx = rel_x+.75, rely = rel_y+.42, anchor = N)

        self.letter25 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter25.place(relx = rel_x, rely = rel_y+.56, anchor = N)
        self.letter26 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter26.place(relx = rel_x + 0.15, rely = rel_y+.56, anchor = N)
        self.letter27= Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter27.place(relx = rel_x +.3, rely = rel_y+.56, anchor = N)
        self.letter28 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter28.place(relx = rel_x+.45, rely = rel_y+.56, anchor = N)
        self.letter29 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter29.place(relx = rel_x+.6, rely = rel_y+.56, anchor = N)
        self.letter30 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter30.place(relx = rel_x+.75, rely = rel_y+.56, anchor = N)

        self.letter31 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter31.place(relx = rel_x, rely = rel_y+.70, anchor = N)
        self.letter32 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter32.place(relx = rel_x + 0.15, rely = rel_y+.70, anchor = N)
        self.letter33= Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter33.place(relx = rel_x +.3, rely = rel_y+.70, anchor = N)
        self.letter34 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter34.place(relx = rel_x+.45, rely = rel_y+.70, anchor = N)
        self.letter35 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter35.place(relx = rel_x+.6, rely = rel_y+.70, anchor = N)
        self.letter36 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.letter36.place(relx = rel_x+.75, rely = rel_y+.70, anchor = N)
            
        
        self.testletter = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#DDBEA9")
        self.testletter.place(relx = .80, rely = .90, anchor = N)

    def retrieve_word1(self, event=None):

        l1 = self.letter1.get(1.0, "end-1c")
        l2 = self.letter2.get(1.0, "end-1c")
        l3 = self.letter3.get(1.0, "end-1c")
        l4 = self.letter4.get(1.0, "end-1c")
        l5 = self.letter5.get(1.0, "end-1c")
        l6 = self.letter6.get(1.0, "end-1c")

        word = l1 + l2 + l3 + l4 + l5 + l6
        print(word)


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
        

        
    

