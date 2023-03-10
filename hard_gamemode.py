# comments for these are written on intermediate_gamemode.py
from tkinter import *
import tkinter
#from PIL import Image, ImageTk
import random
from tkinter import messagebox as mb
from tkinter import simpledialog
from os import path

class Hard(Frame):
    def __init__(self, master):
        super(Hard, self).__init__(master)
        self.create_widgets_h(master)
        self.file = ("midyear_6letterwords.txt")
        self.choose_word(self.file)
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

        self.correct = [False, False, False, False, False, False]
        print(self.hardword)

    def create_widgets_h(self, root):
        root.geometry("450x640")
        root.maxsize(450, 640)
        root.config(bg = "#6B705C")

        self.button2 = Button(root, command = self.onclick_change, width = 50, height = 600, bg = '#fcba03')

        self.frame = Frame(root, width = 350, height = 520, bg = "#A5A58D")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)

        Label(self.frame, text = "HARD MODE", font=("Consolas", 16), bg = "#A5A58D").place(relx = 0.5, rely = 0.05, anchor = N)
        self.button_bg = Button(self.frame, command = self.retrieve_word1, width = 15, height = 2, text='Guess', bg = '#DDBEA9')
        self.hint_btn = Button(self.frame, command=self.request_hint, width=3, height=2, text='Hint', bg='#0000FF', fg='#ffffff')

        rel_x = .12

        rel_y = .14
        
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
        self.button_bg.place(relx = 0.5, rely = rel_y+.75, anchor = N)
        self.hint_btn.place(relx = 0.85, rely = rel_y+.75, anchor = N)


    def request_hint(self):
        open(path.expanduser('~/.wordlescore'), 'a+').close()
        with open(path.expanduser('~/.wordlescore'), 'r+') as file:
            score = file.read().strip()
            try:
                score = int(score)
            except:
                file.write('0')
                score = 0
        if score < 150:
            self.winfo_toplevel().attributes('-topmost', False)
            mb.showerror("Too few points", f"A hint costs 150 points. You only have {score} points")
            self.winfo_toplevel().attributes('-topmost', True)
            return

        self.winfo_toplevel().attributes('-topmost', False)
        answer = mb.askyesno('Confirm Hint Purchase for 150 Points',
            'Are you sure you want to buy a hint for 150 points? ' +
            f'Your balance after this transaction will be {score - 150} points')
        if not answer:
            mb.showinfo('Canceled', 'The transaction has been canceled.')
        else:
            open(path.expanduser('~/.wordlescore'), 'a+').close()
            with open(path.expanduser('~/.wordlescore'), 'r+') as file:
                file.seek(0)
                file.write(str(score - 150))
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
                mb.showinfo(f'Letter {n}', f'Letter {n} is: {self.hardword[n - 1]}')
                break
        self.winfo_toplevel().attributes('-topmost', True)

    def retrieve_word1(self):

        for i in range(36):
            setattr(self, f'letter{i + 1}r', getattr(self, f'letter{i + 1}').get(1.0, 'end-1c'))

        word = ''

        i = 0
        for letters in [[self.letter1r, self.letter2r, self.letter3r, self.letter4r,
            self.letter5r, self.letter6r], [self.letter7r, self.letter8r, self.letter9r,
            self.letter10r, self.letter11r, self.letter12r], [self.letter13r, self.letter14r,
            self.letter15r, self.letter16r, self.letter17r, self.letter18r], [self.letter19r,
            self.letter20r, self.letter21r, self.letter22r, self.letter23r, self.letter24r],
            [self.letter25r, self.letter26r, self.letter27r, self.letter28r, self.letter29r,
            self.letter30r], [self.letter31r, self.letter32r, self.letter33r, self.letter34r,
            self.letter35r, self.letter36r]]:
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
        if word.lower() == self.hardword:
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
            mb.showinfo("You win!!!", f"You got the word correct in {self.curword + 1} tries: {self.hardword}.\n" + "You have gained 250 points!")
            self.winfo_toplevel().destroy()
        else:
            self.button_bg.configure(state=tkinter.DISABLED)
            self.button2.configure(state=tkinter.DISABLED)

            i = 0
            for l in word.lower():
                print(i, l)
                if self.hardword[i] != l and self.correct[i]:
                    self.winfo_toplevel().attributes('-topmost', False)
                    ending = 'rd'
                    if i == 0:
                        ending = 'st'
                    mb.showinfo("Can't change correct letter",
                        f"The {i + 1}{ending} letter ({self.hardword[i]}) was correct last attempt. " +
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
                if self.hardword[i] == l:
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
                if self.hardword[i] != l and l in self.hardword and seen[l] < self.hardword.count(l):
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
                mb.showinfo("Game over", f"You lost. The word was: {self.hardword}")
                self.winfo_toplevel().destroy()
                return
            self.button_bg.configure(state=tkinter.NORMAL)
            self.button2.configure(state=tkinter.NORMAL)


    def onclick_change(self, event=None):
        self.letter1.tag_add(f'{self.letter1r}')
        self.letter1.tag_config(f'{self.letter1r}', background = 'green', foreground = 'white')
