from tkinter import *
from PIL import Image, ImageTk
import random

class Intermediate(Frame):

    def __init__(self, master):

        super(Intermediate, self).__init__(master)
        self.create_widgets()
        self.file = ("midyear_5letterwords.txt")

    def choose_word(self, file): 

        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.intword = self.fiveletterlist([random.randint(0, 1000)])

    def create_widgets(self):

        root.geometry("400x600")
        root.maxsize(400, 600)
        root.config(bg = "#F8EDEB") # I'LL CHANGE BG LATER

        self.frame = Frame(root, width = 400, height = 600, bg = "#F9DCC4") # I'LL CHANGE BG LATER
        self.frame.place(x = 0, y = 0)

        Label(self.frame, text = "INTERMEDIATE MODE", font=("Consolas", 13), bg = "pink").place(relx = 0.5, rely = 0.05, anchor = N) # vivian i will change the color later, i can't rn bc i have no wifi

        rel_x = 0.1
        rel_y = 0.14

        for i in range(1,6):
            self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#CDB4DB") # I'LL CHANGE BG LATER
            self.letter1.place(relx = rel_x, rely = rel_y, anchor = N)

            self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#CDB4DB") # I'LL CHANGE BG LATER
            self.letter2.place(relx = rel_x * 3, rely = rel_y, anchor = N)
            self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#CDB4DB") # I'LL CHANGE BG LATER
            self.letter3.place(relx = rel_x * 5, rely = rel_y, anchor = N)
            self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#CDB4DB") # I'LL CHANGE BG LATER
            self.letter4.place(relx = rel_x *7, rely = rel_y, anchor = N)
            self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#CDB4DB") # I'LL CHANGE BG LATER
            self.letter5.place(relx = rel_x * 9, rely = rel_y, anchor = N)

            rel_y += 0.14

            self.image = Image.open("peachimage.png")
            resize_image = self.image.resize((20, 20))
            img = ImageTk.PhotoImage(resize_image)
            peach_lbl=Label(image=img)
            peach_lbl.image = img
            peach_lbl.place(x=100,y=100)
       
 #def retrieve_word1(self, event):

        #l1 = self.letter1.get(1.0, "end-1c")
        #l2 = self.letter2.get(1.0, "end-1c")
        #l3 = self.letter3.get(1.0, "end-1c")
        #l4 = self.letter4.get(1.0, "end-1c")
        #l5 = self.letter5.get(1.0, "end-1c")
        #l6 = self.letter6.get(1.0, "end-1c")

        #word = l1 + l2 + l3 + l4 + l5 + l6
        #return word

root = Tk() 

#root.bind('<Return, retrieve_word1')

root.title("Intermediate Mode")
app = Intermediate(root)
root.mainloop()