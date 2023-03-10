from tkinter import *
from easy_gamemode import Easy
from intermediate_gamemode import Intermediate
from hard_gamemode import Hard
from os import path
# import everything for tkinter and all that
class Application(Frame):

    def __init__(self, master):
# make the attributes i think for like each screen, each gamemode 
        super(Application, self).__init__(master)
        self.create_widgets()
        self.easy_screen = None
        self.intermediate_screen = None
        self.hard_screen = None
        self.shop_screen = None

    def update_score(self):
        open(path.expanduser('~/.wordlescore'), 'a+').close()
        with open(path.expanduser('~/.wordlescore'), 'r+') as file:
            score = file.read().strip()
            try:
                score = int(score)
            except:
                file.write('0')
                score = 0
                #create label for the score
            self.score_label.configure(text=f'Points: {score}')
        self.after(2500, self.update_score)
# have a way to update the score in homepage

    def create_widgets(self):
        canvas = Canvas()
# print out the menu screen, the selection buttons for each gamemode
        Label(root, text = "W♾RDLE", font=("Consolas", 30), fg = "black").place(x=110,y=1)
        Button(root, text = " EASY ", command = self.setup_easy, font =("Consolas", 15), fg = "black", bg = "#F9DCC4", width=13, height=1).place(x=220,y=65)
        Button(root, text = "INTERMEDIATE", command = self.setup_intermediate, font =("Consolas", 15), fg = "white", bg= "#6191BF", width=13, height=1).place(x=220, y=115)
        Button(root, text = " HARD ", command = self.setup_hard, font =("Consolas", 15), fg = "white", bg = "#3E824B", width=13, height=1).place(x=220,y=165)
        Label(root, text = "Gamemode", font=("Consolas", 20), fg = "black").place(x=50,y=70)
        Label(root, text = "Choose a gamemode", font=("Consolas", 10), fg = "black").place(x=50,y=120)
        Label(root, text = "to the right.", font=("Consolas", 10), fg = "black").place(x=60,y=140)
# label for our score keeper, along with the print outs for the instructions!!!!
        self.score_label = Label(root, text='Points: --', font=('Consolas', 12), fg='black', bg='#EAE37F')
        self.score_label.place(x=55, y=180)
        Label(root, text = "Instructions", font=("Consolas", 20), fg = "black").place(x=30,y=250)
        Label(root, text = "How to Play", font=("Consolas", 13), fg = "black").place(x=30,y=285)
        Label(root, text = "Wordle is a puzzle game that allows the users to puzzle", font=("Consolas", 8), fg = "black").place(x=30,y=320)
        Label(root, text = "out what the randomly chosen word is. The word has a certain", font=("Consolas", 8), fg = "black").place(x=22,y=340)
        Label(root, text = "number of letters, depending on the gamemode chosen. The", font=("Consolas", 8), fg = "black").place(x=30,y=360)
        Label(root, text = "EASY gamemode makes the user guess 4-letter words. The INTERMEDIATE", font=("Consolas", 7), fg = "black").place(x=23,y=380)
        Label(root, text = "gamemode makes the user guess 5-letter words, and the HARD", font=("Consolas", 8), fg = "black").place(x=28,y=400)
        Label(root, text = "mode, 6-letter words. Once a difficulty is chosen, the user", font=("Consolas", 8), fg = "black").place(x=22,y=420)
        Label(root, text = "could start guessing the word. The correctly inputted letters", font=("Consolas", 8), fg = "black").place(x=22,y=440)
        Label(root, text = "turn green, the letters that are in the wrong place but", font=("Consolas", 8), fg = "black").place(x=30,y=460)
        Label(root, text = "somewhere in the word turn yellow, and the completely wrong", font=("Consolas", 8), fg = "black").place(x=22,y=480)
        Label(root, text = "letters turn gray. Try your best to guess the word, have fun!", font=("Consolas", 8), fg = "black").place(x=22,y=500)

# to make it extra fancy i added a coupe borders from lines and dotted lines
        canvas.create_line(2, 27, 500, 27, width=2)
        canvas.create_line(2, 230, 500, 230, width=2)

        canvas.create_line(2, 22, 500, 22, dash=(7), width=2)
        canvas.create_line(2, 235, 500, 235, dash=(7), width=2)
        canvas.pack()

# make sure to update score !!!!!!! stays up to date
        self.update_score()
        
    # this is basically just to take you from homepage to each of the game mode pages!  
    def setup_easy(self):
        root = Tk()
        root.attributes('-topmost', True)
        root.title("EASY MODE")
        app = Easy(root)

    def setup_intermediate(self):
        root = Tk()
        root.attributes('-topmost', True)
        root.title("INTERMEDIATE MODE")
        app = Intermediate(root)

    def setup_hard(self):
        root = Tk()
        root.attributes('-topmost', True)
        root.title("HARD MODE")
        app = Hard(root)
# except shop page does not actually exist
    def setup_shop(self):
        pass

root = Tk()
root.title("W♾RDLE - Home Page")
root.geometry("400x600")
app = Application(root)
app.mainloop()
