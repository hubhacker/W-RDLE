from tkinter import *
import tkinter
#from PIL import Image, ImageTk
import random
from tkinter import messagebox as mb

class Hard(Frame):

    def __init__(self, master):
        super(Hard, self).__init__(master)
        self.file = ("midyear_6letterwords.txt")
        self.choose_word(self.file)
        self.create_widgets_h(master)
        self.curword = 0

    def choose_word(self, file):

        sixletter = open(file)

        self.sixletterlist = []

        for word in sixletter:
            word = word.strip()
            self.sixletterlist.append(word)

        rng = random.randint(0, 1000)

        self.hardword = self.sixletterlist[rng]

        self.hardword_split = []
        for i in self.hardword:
            self.hardword_split.append(i)

        print(self.hardword)

    def create_widgets_h(self, root):
#        canvas = Canvas()
        root.geometry("450x640")
        root.maxsize(450, 640)
        root.config(bg = "#6B705C")

        self.button_bg = Button(root, command = self.retrieve_word1, width = 400, height = 600, bg = '#DDBEA9').place(x= 0, y = 0, relx = 0, rely= 0)
        self.button2 = Button(root, command = self.onclick_change, width = 50, height = 600, bg = '#fcba03').place(x= 0, y= 0, relx = 0, rely = 0)

        self.frame = Frame(root, width = 350, height = 520, bg = "#A5A58D")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)



        Label(self.frame, text = "HARD MODE", font=("Consolas", 16), bg = "#A5A58D").place(relx = 0.5, rely = 0.05, anchor = N)

        rel_x = .12

        rel_y = .14

        #Button(self., text = " test ", command = self.retrieve_word1, font =("Consolas", 15), fg = "black", bg = "#F9DCC4", width=13, height=1).place(relx = .85, rely = .90, anchor = N)

        self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6")
        self.letter1.place(relx = rel_x, rely = rel_y, anchor = N)
        self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6")
        self.letter2.place(relx = rel_x + 0.15, rely = rel_y, anchor = N)
        self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6")
        self.letter3.place(relx = rel_x +.3, rely = rel_y, anchor = N)
        self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6")
        self.letter4.place(relx = rel_x+.45, rely = rel_y, anchor = N)
        self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6")
        self.letter5.place(relx = rel_x+.6, rely = rel_y, anchor = N)
        self.letter6 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6")
        self.letter6.place(relx = rel_x+.75, rely = rel_y, anchor = N)

        self.letter7 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter7.place(relx = rel_x, rely = rel_y+.13, anchor = N)
        self.letter8 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter8.place(relx = rel_x + 0.15, rely = rel_y+.13, anchor = N)
        self.letter9 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter9.place(relx = rel_x +.3, rely = rel_y+.13, anchor = N)
        self.letter10 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter10.place(relx = rel_x+.45, rely = rel_y+.13, anchor = N)
        self.letter11 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter11.place(relx = rel_x+.6, rely = rel_y+.13, anchor = N)
        self.letter12 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter12.place(relx = rel_x+.75, rely = rel_y+.13, anchor = N)

        self.letter13 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter13.place(relx = rel_x, rely = rel_y+.25, anchor = N)
        self.letter14 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter14.place(relx = rel_x + 0.15, rely = rel_y+.25, anchor = N)
        self.letter15 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter15.place(relx = rel_x +.3, rely = rel_y+.25, anchor = N)
        self.letter16 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter16.place(relx = rel_x+.45, rely = rel_y+.25, anchor = N)
        self.letter17 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter17.place(relx = rel_x+.6, rely = rel_y+.25, anchor = N)
        self.letter18 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter18.place(relx = rel_x+.75, rely = rel_y+.25, anchor = N)


        self.letter19 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter19.place(relx = rel_x, rely = rel_y+.37, anchor = N)
        self.letter20 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter20.place(relx = rel_x + 0.15, rely = rel_y+.37, anchor = N)
        self.letter21 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter21.place(relx = rel_x +.3, rely = rel_y+.37, anchor = N)
        self.letter22 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter22.place(relx = rel_x+.45, rely = rel_y+.37, anchor = N)
        self.letter23 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter23.place(relx = rel_x+.6, rely = rel_y+.37, anchor = N)
        self.letter24 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter24.place(relx = rel_x+.75, rely = rel_y+.37, anchor = N)

        self.letter25 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter25.place(relx = rel_x, rely = rel_y+.49, anchor = N)
        self.letter26 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter26.place(relx = rel_x + 0.15, rely = rel_y+.49, anchor = N)
        self.letter27= Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter27.place(relx = rel_x +.3, rely = rel_y+.49, anchor = N)
        self.letter28 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter28.place(relx = rel_x+.45, rely = rel_y+.49, anchor = N)
        self.letter29 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter29.place(relx = rel_x+.6, rely = rel_y+.49, anchor = N)
        self.letter30 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter30.place(relx = rel_x+.75, rely = rel_y+.49, anchor = N)

        self.letter31 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter31.place(relx = rel_x, rely = rel_y+.61, anchor = N)
        self.letter32 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter32.place(relx = rel_x + 0.15, rely = rel_y+.61, anchor = N)
        self.letter33= Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter33.place(relx = rel_x +.3, rely = rel_y+.61, anchor = N)
        self.letter34 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter34.place(relx = rel_x+.45, rely = rel_y+.61, anchor = N)
        self.letter35 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter35.place(relx = rel_x+.6, rely = rel_y+.61, anchor = N)
        self.letter36 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#FFE8D6", state='disabled')
        self.letter36.place(relx = rel_x+.75, rely = rel_y+.61, anchor = N)


    def retrieve_word1(self):

        self.letter1r = self.letter1.get(1.0, "end-1c")
        self.letter2r = self.letter2.get(1.0, "end-1c")
        self.letter3r = self.letter3.get(1.0, "end-1c")
        self.letter4r = self.letter4.get(1.0, "end-1c")
        self.letter5r = self.letter5.get(1.0, "end-1c")
        self.letter6r = self.letter6.get(1.0, "end-1c")
        self.letter1.configure(state='disabled')
        self.letter2.configure(state='disabled')
        self.letter3.configure(state='disabled')
        self.letter4.configure(state='disabled')
        self.letter5.configure(state='disabled')
        self.letter6.configure(state='disabled')

        self.letter7r = self.letter1.get(1.0, "end-1c")
        self.letter8r = self.letter2.get(1.0, "end-1c")
        self.letter9r = self.letter3.get(1.0, "end-1c")
        self.letter10r = self.letter4.get(1.0, "end-1c")
        self.letter11r = self.letter5.get(1.0, "end-1c")
        self.letter12r = self.letter6.get(1.0, "end-1c")

        self.letter13r = self.letter1.get(1.0, "end-1c")
        self.letter14r = self.letter2.get(1.0, "end-1c")
        self.letter15r = self.letter3.get(1.0, "end-1c")
        self.letter16r = self.letter4.get(1.0, "end-1c")
        self.letter17r = self.letter5.get(1.0, "end-1c")
        self.letter18r = self.letter6.get(1.0, "end-1c")

        self.letter19r = self.letter1.get(1.0, "end-1c")
        self.letter20r = self.letter2.get(1.0, "end-1c")
        self.letter21r = self.letter3.get(1.0, "end-1c")
        self.letter22r = self.letter4.get(1.0, "end-1c")
        self.letter23r = self.letter5.get(1.0, "end-1c")
        self.letter24r = self.letter6.get(1.0, "end-1c")

        self.letter25r = self.letter1.get(1.0, "end-1c")
        self.letter26r = self.letter2.get(1.0, "end-1c")
        self.letter27r = self.letter3.get(1.0, "end-1c")
        self.letter28r = self.letter4.get(1.0, "end-1c")
        self.letter29r = self.letter5.get(1.0, "end-1c")
        self.letter30r = self.letter6.get(1.0, "end-1c")

        self.letter31r = self.letter1.get(1.0, "end-1c")
        self.letter32r = self.letter2.get(1.0, "end-1c")
        self.letter33r = self.letter3.get(1.0, "end-1c")
        self.letter34r = self.letter4.get(1.0, "end-1c")
        self.letter35r = self.letter5.get(1.0, "end-1c")
        self.letter36r = self.letter6.get(1.0, "end-1c")

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

#root = Tk()

#root.bind('<Return>, retrieve_word1')

#root.title("Hard")
#app = Hard(root)
#root.mainloop()
