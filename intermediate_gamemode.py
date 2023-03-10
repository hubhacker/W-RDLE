from tkinter import *
import tkinter
#from PIL import Image, ImageTk
import random
from tkinter import messagebox as mb
from tkinter import simpledialog
from os import path

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

        self.intermediateword = self.fiveletterlist[rng]

        self.intermediateword_split = []
        for i in self.intermediateword:
            self.intermediateword_split.append(i)

        self.correct = [False, False, False, False, False, False]
        print(self.intermediateword)

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
       
    def request_hint(self):
        open(path.expanduser('~/.wordlescore'), 'a+').close()
        with open(path.expanduser('~/.wordlescore'), 'r+') as file:
            score = file.read().strip()
            try:
                score = int(score)
            except:
                file.write('0')
                score = 0
        if score < 250:
            self.winfo_toplevel().attributes('-topmost', False)
            mb.showerror("Too few points", f"A hint costs 250 points. You only have {score} points")
            self.winfo_toplevel().attributes('-topmost', True)
            return

        self.winfo_toplevel().attributes('-topmost', False)
        answer = mb.askyesno('Confirm Hint Purchase for 250 Points',
            'Are you sure you want to buy a hint for 250 points? ' +
            f'Your balance after this transaction will be {score - 250} points')
        if not answer:
            mb.showinfo('Canceled', 'The transaction has been canceled.')
        else:
            open(path.expanduser('~/.wordlescore'), 'a+').close()
            with open(path.expanduser('~/.wordlescore'), 'r+') as file:
                file.seek(0)
                file.write(str(score - 250))
                file.truncate()
            while True:
                n = simpledialog.askstring('Letter', 'Which letter do you want to reveal? (1, 2, 3, 4, 5, or 6)?')
                if n not in ['1', '2', '3', '4', '5', '6']:
                    mb.showinfo('Invalid', 'Invalid input')
                    continue
                n = int(n)
                if self.correct[n - 1]:
                    mb.showinfo('Already Correct', f'You already have letter {n} correct.')
                    continue
                mb.showinfo(f'Letter {n}', f'Letter {n} is: {self.intermediateword[n - 1]}')
                break
        self.winfo_toplevel().attributes('-topmost', True)

    def retrieve_word1(self):

        for i in range(36):
            setattr(self, f'letter{i + 1}r', getattr(self, f'letter{i + 1}').get(1.0, 'end-1c'))

        word = ''

        i = 0
        for letters in [[self.letter1r, self.letter2r, self.letter3r, self.letter4r,
            self.letter5r], [self.letter6r, self.letter7r, self.letter8r,
            self.letter9r, self.letter10r], [self.letter11r, self.letter12r,
            self.letter13r, self.letter14r, self.letter15r], [self.letter16r,
            self.letter17r, self.letter18r, self.letter19r, self.letter20r],
            [self.letter21r, self.letter22r, self.letter23r, self.letter24r, self.letter25r], 
            [self.letter26r, self.letter27r, self.letter28r, self.letter29r,
            self.letter30r]]:
            if i != self.curword:
                i += 1
                continue

            i += 1

            for letter in letters:
                if len(letter) > 1:
                    self.winfo_toplevel().attributes('-topmost', False)
                    mb.showerror("Too Long", "Input cannot be longer than a letter")
                    self.winfo_toplevel().attributes('-topmost', True)

                    return
                elif len(letter) == 0:
                    self.winfo_toplevel().attributes('-topmost', False)
                    mb.showerror("Too Short", "You did not finish the word")
                    self.winfo_toplevel().attributes('-topmost', True)
                    return
                if letter not in __import__('string').ascii_lowercase:
                    self.winfo_toplevel().attributes('-topmost', False)
                    mb.showerror("Bad Letter", "Invalid letter")
                    self.winfo_toplevel().attributes('-topmost', True)
                    return
                word += letter

        print('try', word, self.curword)
        self.check_guess(word)


    def maxlength(sv):
        if len(sv.get()) > 1:
            sv.set(sv.get()[0])
    def check_guess(self, word):
        if word.lower() == self.intermediateword:
            self.winfo_toplevel().attributes('-topmost', False)
            open(path.expanduser('~/.wordlescore'), 'a+').close()
            with open(path.expanduser('~/.wordlescore'), 'r+') as file:
                score = file.read().strip()
                try:
                    score = int(score)
                except:
                    file.write('0')
                    score = 0
                file.seek(0)
                file.write(str(score + 250))
            conj = 'y'
            if self.curword + 1 != 1:
                conj = 'ies'
            mb.showinfo("You win!!!", f"You got the word correct in {self.curword + 1} tr{conj}: {self.intermediateword}.\n" + "You have gained 250 points!")
            self.winfo_toplevel().destroy()
        else:
            self.button_bg.configure(state=tkinter.DISABLED)
            self.button2.configure(state=tkinter.DISABLED)

            i = 0
            for l in word.lower():
                print(i, l)
                if self.intermediateword[i] != l and self.correct[i]:
                    self.winfo_toplevel().attributes('-topmost', False)
                    ending = 'rd'
                    if i == 0:
                        ending = 'st'
                    mb.showinfo("Can't change correct letter",
                        f"The {i + 1}{ending} letter ({self.intermediateword[i]}) was correct last attempt. " +
                        "You can't change it to an incorrect one now.")
                    self.button_bg.configure(state = tkinter.NORMAL)
                    self.button2.configure(state = tkinter.NORMAL)
                    return
                i += 1
            i = 0
            seen = {}
            for letter in __import__('string').ascii_lowercase:
                seen[letter] = 0
            for l in word.lower():
                if self.intermediateword[i] == l:
                    self.correct[i] = True
                    getattr(self, 'letter' + str((self.curword * 6) + (i + 1))).configure(bg='#00ff00')
                    if l in seen:
                        seen[l] += 1
                    else:
                        seen[l] = 1

                else:
                    getattr(self, 'letter' + str((self.curword * 6) + (i + 1))).configure(bg='#808080')
                i += 1
            i = 0
            for l in word.lower():
                if self.intermediateword[i] != l and l in self.intermediateword and seen[l] < self.intermediateword.count(l):
                    getattr(self, 'letter' + str((self.curword * 6) + (i + 1))).configure(bg='#ffff00')
                    if l in seen:
                        seen[l] += 1
                    else:
                        seen[l] = 1
                i += 1
            self.curword += 1
            if self.curword == 1:
                self.letter1.configure(state='disabled')
                self.letter2.configure(state='disabled')
                self.letter3.configure(state='disabled')
                self.letter4.configure(state='disabled')
                self.letter5.configure(state='disabled')
                self.letter6.configure(state='disabled')

                self.letter7.configure(state='normal')
                self.letter8.configure(state='normal')
                self.letter9.configure(state='normal')
                self.letter10.configure(state='normal')
                self.letter11.configure(state='normal')
                self.letter12.configure(state='normal')
            elif self.curword == 2:
                self.letter7.configure(state='disabled')
                self.letter8.configure(state='disabled')
                self.letter9.configure(state='disabled')
                self.letter10.configure(state='disabled')
                self.letter11.configure(state='disabled')
                self.letter12.configure(state='disabled')

                self.letter13.configure(state='normal')
                self.letter14.configure(state='normal')
                self.letter15.configure(state='normal')
                self.letter16.configure(state='normal')
                self.letter17.configure(state='normal')
                self.letter18.configure(state='normal')
            elif self.curword == 3:
                self.letter13.configure(state='disabled')
                self.letter14.configure(state='disabled')
                self.letter15.configure(state='disabled')
                self.letter16.configure(state='disabled')
                self.letter17.configure(state='disabled')
                self.letter18.configure(state='disabled')

                self.letter19.configure(state='normal')
                self.letter20.configure(state='normal')
                self.letter21.configure(state='normal')
                self.letter22.configure(state='normal')
                self.letter23.configure(state='normal')
                self.letter24.configure(state='normal')
            elif self.curword == 4:
                self.letter19.configure(state='disabled')
                self.letter20.configure(state='disabled')
                self.letter21.configure(state='disabled')
                self.letter22.configure(state='disabled')
                self.letter23.configure(state='disabled')
                self.letter24.configure(state='disabled')

                self.letter25.configure(state='normal')
                self.letter26.configure(state='normal')
                self.letter27.configure(state='normal')
                self.letter28.configure(state='normal')
                self.letter29.configure(state='normal')
                self.letter30.configure(state='normal')
            elif self.curword == 5:
                self.letter25.configure(state='disabled')
                self.letter26.configure(state='disabled')
                self.letter27.configure(state='disabled')
                self.letter28.configure(state='disabled')
                self.letter29.configure(state='disabled')
                self.letter30.configure(state='disabled')

                self.letter31.configure(state='normal')
                self.letter32.configure(state='normal')
                self.letter33.configure(state='normal')
                self.letter34.configure(state='normal')
                self.letter35.configure(state='normal')
                self.letter36.configure(state='normal')
            elif self.curword == 6:
                self.letter31.configure(state='disabled')
                self.letter32.configure(state='disabled')
                self.letter33.configure(state='disabled')
                self.letter34.configure(state='disabled')
                self.letter35.configure(state='disabled')
                self.letter36.configure(state='disabled')

                self.winfo_toplevel().attributes('-topmost', False)
                mb.showinfo("Game over", f"You lost. The word was: {self.intermediateword}")
                self.winfo_toplevel().destroy()
                return
            self.button_bg.configure(state=tkinter.NORMAL)
            self.button2.configure(state=tkinter.NORMAL)


    def onclick_change(self, event=None):
        self.letter1.tag_add(f'{self.letter1r}')
        self.letter1.tag_config(f'{self.letter1r}', background = 'green', foreground = 'white')


