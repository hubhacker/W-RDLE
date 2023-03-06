from tkinter import *
from PIL import Image, ImageTk
import random

class Easy(Frame):

    def __init__(self,master):

        super(Easy, self).__init__(master)
        self.create_widgets()
        self.file=("midyear_4letterwords.txt")
    
    def choose_word(self): 

        fourletter = open("midyear_4letterwords.txt")

        self.fourletterlist = []

        for word in fourletter:
            word = word.strip()
            self.fourletterlist.append(word)

        rng = random.randint(0, 1000)

        self.easyword = self.fourletterlist[rng]
        
        self.easyword_split = []
        for i in self.easyword:
            self.easyword_split.append(i)

        print(self.easyword)

    
    def create_widgets(self):

        
        root.geometry("400x600")
        root.maxsize(400, 600)
        root.config(bg = "#F8EDEB")

        self.frame = Frame(root, width = 300, height = 440, bg = "#F9DCC4")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)

        Label(self.frame, text = "EASY MODE", font=("Consolas", 13), bg = "#F9DCC4").place(relx = 0.5, rely = 0.05, anchor = N)

        self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter1.place(relx = 0.2, rely = 0.14, anchor = N)
        self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter2.place(relx = 0.4, rely = 0.14, anchor = N)
        self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter3.place(relx = 0.6, rely = 0.14, anchor = N)
        self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter4.place(relx = 0.8, rely = 0.14, anchor = N)

        self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter5.place(relx = 0.2, rely = 0.28, anchor = N)
        self.letter6 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter6.place(relx = 0.4, rely = 0.28, anchor = N)
        self.letter7 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter7.place(relx = 0.6, rely = 0.28, anchor = N)
        self.letter8 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter8.place(relx = 0.8, rely = 0.28, anchor = N)

        self.letter9 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter9.place(relx = 0.2, rely = 0.41, anchor = N)
        self.letter10 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter10.place(relx = 0.4, rely = 0.41, anchor = N)
        self.letter11 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter11.place(relx = 0.6, rely = 0.41, anchor = N)
        self.letter12 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter12.place(relx = 0.8, rely = 0.41, anchor = N)
        
        self.letter13 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter13.place(relx = 0.2, rely = 0.54, anchor = N)
        self.letter14 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter14.place(relx = 0.4, rely = 0.54, anchor = N)
        self.letter15 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter15.place(relx = 0.6, rely = 0.54, anchor = N)
        self.letter16 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter16.place(relx = 0.8, rely = 0.54, anchor = N)
        
        self.letter17 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter17.place(relx = 0.2, rely = 0.67, anchor = N)
        self.letter18 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter18.place(relx = 0.4, rely = 0.67, anchor = N)
        self.letter19 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter19.place(relx = 0.6, rely = 0.67, anchor = N)
        self.letter20 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter20.place(relx = 0.8, rely = 0.67, anchor = N)
        
        self.letter21 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter21.place(relx = 0.2, rely = 0.80, anchor = N)
        self.letter22 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter22.place(relx = 0.4, rely = 0.80, anchor = N)
        self.letter23 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter23.place(relx = 0.6, rely = 0.80, anchor = N)
        self.letter24 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter24.place(relx = 0.8, rely = 0.80, anchor = N)

        self.image = Image.open("peachimage.png")
        resize_image = self.image.resize((30, 40))
#        self.image=PhotoImage(file='peachimage.png')
#        img = self.image.PhotoImage(resize_image)
        img = ImageTk.PhotoImage(resize_image)
        peach_lbl=Label(image=img)
        peach_lbl.image = img
        peach_lbl.place(x=110,y=80)

        self.image2 = Image.open("peach.jpg")
        resize_image = self.image2.resize((20, 20))
#        self.image=PhotoImage(file='peachimage.png')
#        img = self.image.PhotoImage(resize_image)
        img2 = ImageTk.PhotoImage(resize_image)
        peach_lbl2=Label(image=img2)
        peach_lbl2.image = img2
        peach_lbl2.place(x=70,y=90)

        self.image3 = Image.open("peachimage.png")
        resize_image = self.image3.resize((30, 40))
#        self.image=PhotoImage(file='peachimage.png')
#        img = self.image.PhotoImage(resize_image)
        img3 = ImageTk.PhotoImage(resize_image)
        peach_lbl=Label(image=img3)
        peach_lbl.image = img3
        peach_lbl.place(x=260,y=80)

        self.image4 = Image.open("peach.jpg")
        resize_image = self.image4.resize((20, 20))
#        self.image=PhotoImage(file='peachimage.png')
#        img = self.image.PhotoImage(resize_image)
        img4 = ImageTk.PhotoImage(resize_image)
        peach_lbl2=Label(image=img4)
        peach_lbl2.image = img4
        peach_lbl2.place(x=310,y=90)

    def checker(self, event=None):
        enter = self.letter4.get('1.0', END)
        lastletter_list = enter.split()
        empty = True
        
        if empty == False:
            pass

    def retrieve_word1(self, event=None):

        self.one = self.letter1.get(1.0, "end-1c")
        self.two = self.letter2.get(1.0, "end-1c")
        self.three = self.letter3.get(1.0, "end-1c")
        self.four = self.letter4.get(1.0, "end-1c")

        word = self.one + self.two + self + self.three + self.four
        print(word)

    def check_guess(self):
        
        if self.one == self.easyword_split[0]:
            self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#3cb542")

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
root.title("EASY MODE")
app = Easy(root)
root.mainloop()