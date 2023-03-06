from tkinter import *
import tkinter
from PIL import Image, ImageTk
import random
#F9DCC4
class Intermediate(Frame):

    def __init__(self, master):

        super(Intermediate, self).__init__(master)
        self.file = ("midyear_5letterwords.txt")
        self.create_widgets_i(master)

    def choose_word(self, file): 

        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.intword = self.fiveletterlist([random.randint(0, 1000)])

    def create_widgets_i(self,root):
        canvas = Canvas()
        root.geometry("450x590")
        root.maxsize(450, 590)
        root.config(bg = "#f0e6ef")

        self.frame = Frame(root, width = 325, height = 430, bg = "#ead5f2") # I'LL CHANGE BG LATER
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)

        Label(self.frame, text = "INTERMEDIATE MODE", font=("Consolas", 15), bg = "#FFC8DD").place(relx = 0.5, rely = 0.05, anchor = N) # vivian i will change the color later, i can't rn bc i have no wifi

        rel_x = 0.17
        rel_y = 0.2

        for i in range(1,6):
            self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#f0e6ef")
            self.letter1.place(relx = rel_x, rely = rel_y, anchor = N)

            self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#f0e6ef") # I'LL CHANGE BG LATER
            self.letter2.place(relx = rel_x * 2, rely = rel_y, anchor = N)
            self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#f0e6ef") # I'LL CHANGE BG LATER
            self.letter3.place(relx = rel_x * 3, rely = rel_y, anchor = N)
            self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#f0e6ef") # I'LL CHANGE BG LATER
            self.letter4.place(relx = rel_x *4, rely = rel_y, anchor = N)
            self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#f0e6ef") # I'LL CHANGE BG LATER
            self.letter5.place(relx = rel_x * 5, rely = rel_y, anchor = N)

            rel_y += 0.14

        # self.image = Image.open("sanrio.png")
        # resize_image = self.image.resize((60, 60))
        # img = ImageTk.PhotoImage(resize_image)
        # peach_lbl=Label(image=img)
        # peach_lbl.image = img
        # peach_lbl.place(x=100,y=103)

        # self.image = Image.open("peachimage.png")
        # resize_image = self.image.resize((20, 20))
        # img = ImageTk.PhotoImage(resize_image)
        # peach_lbl=Label(image=img)
        # peach_lbl.image = img
        # peach_lbl.place(x=302,y=31)
       
 #def retrieve_word1(self, event):

        #l1 = self.letter1.get(1.0, "end-1c")
        #l2 = self.letter2.get(1.0, "end-1c")
        #l3 = self.letter3.get(1.0, "end-1c")
        #l4 = self.letter4.get(1.0, "end-1c")
        #l5 = self.letter5.get(1.0, "end-1c")
        #l6 = self.letter6.get(1.0, "end-1c")

        #word = l1 + l2 + l3 + l4 + l5 + l6
        #return word

#root = Tk() 

#root.bind('<Return, retrieve_word1')

#root.title("Intermediate Mode")
#app = Intermediate(root)
#root.mainloop()