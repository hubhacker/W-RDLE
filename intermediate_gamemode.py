from tkinter import *
import tkinter
from PIL import Image, ImageTk
import random
from tkinter import messagebox as mb
#F9DCC4
class Intermediate(Frame):

    def __init__(self, master):
        super(Intermediate, self).__init__(master)
        self.file = ("midyear_5letterwords.txt")
        self.choose_word(self.file)
        self.create_widgets_i(master)
        self.curwood = 0

    def choose_word(self, file): 

        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            word = word.strip()
            self.fiveletterlist.append(word)

        rng = random.randint(0, 1000)

        self.intword = self.fiveletterlist[rng]

        self.intword_split = []
        for i in self.intword:
            self.intword_split.append(i)

        print(self.intword)

    def create_widgets_i(self,root):
        #canvas = Canvas()
        root.geometry("430x600")
        root.maxsize(429, 600)
        root.config(bg = "#e2eafc")

        self.button_bg = Button(root, command = self.retrieve_word1, width = 400, height = 600, bg = '#e2eafc').place(x= 0, y = 0, relx = 0, rely= 0)
        self.button2 = Button(root, command = self.onclick_change, width = 50, height = 600, bg = '#e2eafc').place(x= 0, y= 0, relx = 0, rely = 0)

        self.frame = Frame(root, width = 350, height = 450, bg = "#BDE0FE")
        self.frame.place(x = 19, y = 20, relx = 0.08, rely = 0.08)

        Label(self.frame, text = "INTERMEDIATE MODE", font=("Consolas", 16), bg = "#BDE0FE").place(relx = 0.5, rely = 0.05, anchor = N)

        rel_x = 0.17

        rel_y = 0.18

        for i in range(1,6):
            self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#e2eafc")
            self.letter1.place(relx = rel_x, rely = rel_y, anchor = N)

            self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#e2eafc") # I'LL CHANGE BG LATER
            self.letter2.place(relx = rel_x * 2, rely = rel_y, anchor = N)
            self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#e2eafc") # I'LL CHANGE BG LATER
            self.letter3.place(relx = rel_x * 3, rely = rel_y, anchor = N)
            self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#e2eafc") # I'LL CHANGE BG LATER
            self.letter4.place(relx = rel_x *4, rely = rel_y, anchor = N)
            self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#e2eafc") # I'LL CHANGE BG LATER
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
       
    def retrieve_word1(self):

        self.letter1r = self.letter1.get(1.0, "end-1c")
        self.letter2r = self.letter2.get(1.0, "end-1c")
        self.letter3r = self.letter3.get(1.0, "end-1c")
        self.letter4r = self.letter4.get(1.0, "end-1c")
        self.letter5r = self.letter5.get(1.0, "end-1c")

        self.letter1.configure(state='disabled')
        self.letter2.configure(state='disabled')
        self.letter3.configure(state='disabled')
        self.letter4.configure(state='disabled')
        self.letter5.configure(state='disabled')


        self.letter6r = self.letter1.get(1.0, "end-1c")
        self.letter7r = self.letter2.get(1.0, "end-1c")
        self.letter8r = self.letter3.get(1.0, "end-1c")
        self.letter9r = self.letter4.get(1.0, "end-1c")
        self.letter10r = self.letter5.get(1.0, "end-1c")


        self.letter11r = self.letter1.get(1.0, "end-1c")
        self.letter12r = self.letter2.get(1.0, "end-1c")
        self.letter13r = self.letter3.get(1.0, "end-1c")
        self.letter14r = self.letter4.get(1.0, "end-1c")
        self.letter15r = self.letter5.get(1.0, "end-1c")


        self.letter16r = self.letter1.get(1.0, "end-1c")
        self.letter17r = self.letter2.get(1.0, "end-1c")
        self.letter18r = self.letter3.get(1.0, "end-1c")
        self.letter19r = self.letter4.get(1.0, "end-1c")
        self.letter20r = self.letter5.get(1.0, "end-1c")


        self.letter21r = self.letter1.get(1.0, "end-1c")
        self.letter22r = self.letter2.get(1.0, "end-1c")
        self.letter23r = self.letter3.get(1.0, "end-1c")
        self.letter24r = self.letter4.get(1.0, "end-1c")
        self.letter25r = self.letter5.get(1.0, "end-1c")

        for letter in [self.letter1r, self.letter2r, self.letter3r, self.letter4r, self.letter5r, self.letter6r]:
            if len(letter) > 1:
                mb.showerror("Too Long", "Input cannot be longer than a letter")
                return
            elif len(letter) == 0:
                mb.showerror("Too Short", "You did not finish the word")
                return

        word = self.letter1r + self.letter2r + self.letter3r + self.letter4r + self.letter5r + self.letter6r

        self.check_guess(word)


    def check_guess(self, word):
        if word == self.hardword:
            mb.showinfo("You win!!!", "You got the word correct")
        else:
            mb.showinfo("Wrong word", "You got the word wrong")

    def onclick_change(self, event=None):
        self.letter1.tag_add(f'{self.letter1r}')
        self.letter1.tag_config(f'{self.letter1r}', background = 'green', foreground = 'white')

#root = Tk() 

#root.bind('<Return, retrieve_word1')

#root.title("Intermediate Mode")
#app = Intermediate(root)
#root.mainloop()