from tkinter import *
import tkinter
#from PIL import Image, ImageTk
import random
from tkinter import messagebox as mb
from tkinter import simpledialog
from os import path
# again import the stuff
class Intermediate(Frame):
    def __init__(self, master):
        super(Intermediate, self).__init__(master)
        self.file = ("midyear_5letterwords.txt")
        self.choose_word(self.file)
        self.create_widgets_i(master)
        self.curword = 0
# choose the file that has 5 letter words
    def choose_word(self, file): 
        fiveletter = open(file)

        self.fiveletterlist = []
# first we need to strip the word list in the file, because u need to extract the actual words from the list to use
        for word in fiveletter:
            word = word.strip()
            self.fiveletterlist.append(word)
# take all of this and add it into our list of actual five letter words
        rng = random.randint(0, 1000)
# to make it a new, random word each time, were gonna use randint so it picks a random one between 1-1000!
        self.intermediateword = self.fiveletterlist[rng]

        self.intermediateword_split = []
        for i in self.intermediateword:
            self.intermediateword_split.append(i)

        self.correct = [False, False, False, False, False, False]
        print(self.intermediateword)
# this is first to set each of our 6 attempts to false, so the game doesnt like instantly end
    def create_widgets_i(self,root):
        #canvas = Canvas()
        root.geometry("450x640")
        root.maxsize(450, 640)
        root.config(bg = "#e2eafc")
# then we wanna set the size for our little page, and were making it 450 by 640 :)
        self.button2 = Button(root, command = self.onclick_change, width = 50, height = 600, bg = '#e2eafc')
# low key forgot what this button does 
        self.frame = Frame(root, width = 350, height = 520, bg = "#bde0fe")
        self.frame.place(x = 20, y = 20, relx = 0.08, rely = 0.08)
# this is the frame, just to make it look more appealing and spacious ig
        Label(self.frame, text = "INTERMEDIATE MODE", font=("Consolas", 16), bg = "#BDE0FE").place(relx = 0.5, rely = 0.05, anchor = N)
        self.button_bg = Button(self.frame, command = self.retrieve_word1, width = 15, height = 2, text='Guess', bg = '#DDBEA9')
        self.hint_btn = Button(self.frame, command=self.request_hint, width=3, height=2, text='Hint', bg='#0000FF', fg='#ffffff')
        rel_x = .12
# these are the buttons that will actually input the guess, and prompt you for a hint that can be found at the bottom of the page screen!
        rel_y = .14

        self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter1.place(relx = 0.1, rely = 0.14, anchor = N)
        self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter2.place(relx = 0.3, rely = 0.14, anchor = N)
        self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter3.place(relx = 0.5, rely = 0.14, anchor = N)
        self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter4.place(relx = 0.7, rely = 0.14, anchor = N)
        self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter5.place(relx = 0.9, rely = 0.14, anchor = N)
# boring just printing all the text boxes out so you can insert letters so just skip over
        self.letter6 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter6.place(relx = 0.1, rely = 0.26, anchor = N)
        self.letter7 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter7.place(relx = 0.3, rely = 0.26, anchor = N)
        self.letter8 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter8.place(relx = 0.5, rely = 0.26, anchor = N)
        self.letter9 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter9.place(relx = 0.7, rely = 0.26, anchor = N)
        self.letter10 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter10.place(relx = 0.9, rely = 0.26, anchor = N)

        self.letter11 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter11.place(relx = 0.1, rely = 0.38, anchor = N)
        self.letter12 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter12.place(relx = 0.3, rely = 0.38, anchor = N)
        self.letter13 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter13.place(relx = 0.5, rely = 0.38, anchor = N)
        self.letter14 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter14.place(relx = 0.7, rely = 0.38, anchor = N)
        self.letter15 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter15.place(relx = 0.9, rely = 0.38, anchor = N)

        self.letter16 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter16.place(relx = 0.1, rely = 0.50, anchor = N)
        self.letter17 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter17.place(relx = 0.3, rely = 0.50, anchor = N)
        self.letter18 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter18.place(relx = 0.5, rely = 0.50, anchor = N)
        self.letter19 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter19.place(relx = 0.7, rely = 0.50, anchor = N)
        self.letter20 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter20.place(relx = 0.9, rely = 0.50, anchor = N)
        
        self.letter21 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter21.place(relx = 0.1, rely = 0.62, anchor = N)
        self.letter22 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter22.place(relx = 0.3, rely = 0.62, anchor = N)
        self.letter23 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter23.place(relx = 0.5, rely = 0.62, anchor = N)
        self.letter24 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter24.place(relx = 0.7, rely = 0.62, anchor = N)
        self.letter25 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter25.place(relx = 0.9, rely = 0.62, anchor = N)

        self.letter26 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter26.place(relx = 0.1, rely = 0.74, anchor = N)
        self.letter27 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter27.place(relx = 0.3, rely = 0.74, anchor = N)
        self.letter28 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter28.place(relx = 0.5, rely = 0.74, anchor = N)
        self.letter29 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter29.place(relx = 0.7, rely = 0.74, anchor = N)
        self.letter30 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB")
        self.letter30.place(relx = 0.9, rely = 0.74, anchor = N)

        self.button_bg.place(relx = 0.4, rely = rel_y+.77, anchor = N)
        self.hint_btn.place(relx = 0.8, rely = rel_y+.77, anchor = N)
    # this is the function for the prompted hint  
    def request_hint(self):
        open(path.expanduser('~/.wordlescore'), 'a+').close()
        # this is gonna create a new path thing that opens another little page just the read out your options
        with open(path.expanduser('~/.wordlescore'), 'r+') as file:
            score = file.read().strip()
            try:
                score = int(score)
                # your score count, also keeps track of whether you can afford a hint so we need to check it first 
            except:
                file.write('0')
                score = 0
        if score < 150:
            # if you dont have a high enough score to afford a hint, it will reject the purchase and allow you to return to the game
            self.winfo_toplevel().attributes('-topmost', False)
            mb.showerror("Too few points", f"A hint costs 150 points. You only have {score} points")
            self.winfo_toplevel().attributes('-topmost', True)
            return
# however, if you have more than 150 points (which is the cost), then it will allow you to continue the transaction !!!!! :O
        self.winfo_toplevel().attributes('-topmost', False)
        answer = mb.askyesno('Confirm Hint Purchase for 150 Points',
        # this is the confirmation, it will prompt you yes or no
            'Are you sure you want to buy a hint for 150 points? ' +
            f'Your balance after this transaction will be {score - 150} points')
        # it also just lets you know what your score will be after the purchase
        if not answer:
            mb.showinfo('Canceled', 'The transaction has been canceled.')
            #you can also just decline and cancel out of the transaction, close out lil tab
        else:
            open(path.expanduser('~/.wordlescore'), 'a+').close()
            with open(path.expanduser('~/.wordlescore'), 'r+') as file:
                file.seek(0)
                # this is going to seek the score count from the tab to the homepage, and reduct 150 from it D:
                file.write(str(score - 150))
                file.truncate()
            while True:
                n = simpledialog.askstring('Letter', 'Which letter do you want to reveal? (1, 2, 3, 4, or 5)?')
                if n not in ['1', '2', '3', '4', '5']:
                    # once the hint is purchased, you can select with letter you would like to have revealed
                    mb.showinfo('Invalid', 'Invalid input')
                    # if you dont pick a good input, it will allow to to go back and try again
                    continue
                n = int(n)
                if self.correct[n - 1]:
                    # if you have already correctly guessed that letter, it will also allow you to return and 'continue'
                    mb.showinfo('Already Correct', f'You already have letter {n} correct.')
                    continue
                # if there is no issue with your input, and you pick a valid letter placement, 
                # we will use {self.intermediateword[n-1]} to find out what letter is in the place that you requested
                mb.showinfo(f'Letter {n}', f'Letter {n} is: {self.intermediateword[n - 1]}')
                break
        self.winfo_toplevel().attributes('-topmost', True)

    def retrieve_word1(self):

        for i in range(30):
            setattr(self, f'letter{i + 1}r', getattr(self, f'letter{i + 1}').get(1.0, 'end-1c'))

        word = ''
# since intermediate mode is 5 letter version, and there are 6 guessed, we need to account for each of the 30 letters 
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
# with each textbox, we have to make sure sneaky people do not enter more than one letter
            for letter in letters:
                if len(letter) > 1:
                    # if the length of the input is more than one letter, it will stop you and force you to return back
                    self.winfo_toplevel().attributes('-topmost', False)
                    mb.showerror("Too Long", "Input cannot be longer than a letter")
                    self.winfo_toplevel().attributes('-topmost', True)

                    return
                
                # on the flip side they jsut decide not to put anything in the textbox, that will also make an error and force them to return
                elif len(letter) == 0:
                    self.winfo_toplevel().attributes('-topmost', False)
                    mb.showerror("Too Short", "You did not finish the word")
                    self.winfo_toplevel().attributes('-topmost', True)
                    return
                
                # now this is just if its not in the valid alphabet like special characters (ex. $, %, ^, *) and then also make an error (this is sarah btw that sounded rlly professional ik!!!)
                if letter not in __import__('string').ascii_lowercase:
                    self.winfo_toplevel().attributes('-topmost', False)
                    mb.showerror("Bad Letter", "Invalid letter")
                    self.winfo_toplevel().attributes('-topmost', True)
                    return
                word += letter
                # this is going to add each letter into the word so we can compare the guessed word to the actual word!

        print('try', word, self.curword)
        self.check_guess(word)
# now this is to check to see if you are right. if it is correct, game ends. if not, continue! no biggie

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
                # once you have guessed the word, 250 points are added to your score
            mb.showinfo("You win!!!", f"You got the word correct in {self.curword + 1} tries: {self.intermediateword}.\n" + "You have gained 250 points!")
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
                        # this is just for a little grammar, to make the ending of this phrase like ird or st whatever i think u get it! 
                    mb.showinfo("Can't change correct letter",
                                # this stops the player from changing a letter even after they guessed it correctly in a green spot.
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
                    # this code keeps all the letters in place, if the letter matches up with the correct words' letters, the color will change
                    getattr(self, 'letter' + str((self.curword * 5) + (i + 1))).configure(bg='#00ff00')
                    if l in seen:
                        seen[l] += 1
                        # if correct it turns green, wrong it turns gray, or like partially correct then yellowy orange 
                    else:
                        seen[l] = 1

                else:
                    getattr(self, 'letter' + str((self.curword * 5) + (i + 1))).configure(bg='#808080')
                i += 1
            i = 0
            for l in word.lower():
                if self.intermediateword[i] != l and l in self.intermediateword and seen[l] < self.intermediateword.count(l):
                    getattr(self, 'letter' + str((self.curword * 5) + (i + 1))).configure(bg='#ffff00')
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

                self.letter6.configure(state='normal')
                self.letter7.configure(state='normal')
                self.letter8.configure(state='normal')
                self.letter9.configure(state='normal')
                self.letter10.configure(state='normal')
            elif self.curword == 2:
                self.letter6.configure(state='disabled')
                self.letter7.configure(state='disabled')
                self.letter8.configure(state='disabled')
                self.letter9.configure(state='disabled')
                self.letter10.configure(state='disabled')

                self.letter11.configure(state='normal')
                self.letter12.configure(state='normal')
                self.letter13.configure(state='normal')
                self.letter14.configure(state='normal')
                self.letter15.configure(state='normal')

            elif self.curword == 3:
                self.letter11.configure(state='disabled')
                self.letter12.configure(state='disabled')
                self.letter13.configure(state='disabled')
                self.letter14.configure(state='disabled')
                self.letter15.configure(state='disabled')

                self.letter16.configure(state='normal')
                self.letter17.configure(state='normal')
                self.letter18.configure(state='normal')
                self.letter19.configure(state='normal')
                self.letter20.configure(state='normal')
            elif self.curword == 4:
                self.letter16.configure(state='disabled')
                self.letter17.configure(state='disabled')
                self.letter18.configure(state='disabled')
                self.letter19.configure(state='disabled')
                self.letter20.configure(state='disabled')

                self.letter21.configure(state='normal')
                self.letter22.configure(state='normal')
                self.letter23.configure(state='normal')
                self.letter24.configure(state='normal')
                self.letter25.configure(state='normal')
            elif self.curword == 5:
                self.letter21.configure(state='disabled')
                self.letter22.configure(state='disabled')
                self.letter23.configure(state='disabled')
                self.letter24.configure(state='disabled')
                self.letter25.configure(state='disabled')

                self.letter26.configure(state='normal')
                self.letter27.configure(state='normal')
                self.letter28.configure(state='normal')
                self.letter29.configure(state='normal')
                self.letter30.configure(state='normal')

            elif self.curword == 6:
                self.letter26.configure(state='disabled')
                self.letter27.configure(state='disabled')
                self.letter28.configure(state='disabled')
                self.letter29.configure(state='disabled')
                self.letter30.configure(state='disabled')

                self.winfo_toplevel().attributes('-topmost', False)
                mb.showinfo("Game over", f"You lost. The word was: {self.intermediateword}")
                # if you run out of attempts, the game will end and tell the user what the word was
                self.winfo_toplevel().destroy()
                # the page will then collapse and allow you to return to the homepage
                return
            self.button_bg.configure(state=tkinter.NORMAL)
            self.button2.configure(state=tkinter.NORMAL)


    def onclick_change(self, event=None):
        self.letter1.tag_add(f'{self.letter1r}')
        self.letter1.tag_config(f'{self.letter1r}', background = 'green', foreground = 'white')


