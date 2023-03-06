from tkinter import *
from game_manager import GameManager

#from easy_gamemode import Easy
#from intermediate_gamemode import Intermediate
#from hard_gamemode import Hard
#from shop import Shop

class Application(Frame):
    def init(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.easy_screen = None
        self.intermediate_screen = None
        self.hard_screen = None
        self.shop_screen = None
        #self.callback_on_easy = callback_on_easy

    def create_widgets(self):
        canvas = Canvas()


        Label(root, text = "W♾RDLE", font=("Consolas", 30), fg = "black").place(x=110,y=1)
        Button(root, text = " EASY ", command = self.setup_easy, font =("Consolas", 15), fg = "black", bg = "#F9DCC4", width=13, height=1).place(x=220,y=65)
        Button(root, text = "MEDIUM", command = self.setup_intermediate, font =("Consolas", 15), fg = "white", bg= "#CDB4DB", width=13, height=1).place(x=220, y=115)
        Button(root, text = " HARD ", command = self.setup_hard, font =("Consolas", 15), fg = "white", bg = "#4f7aa8", width=13, height=1).place(x=220,y=165)
        Label(root, text = "Gamemode", font=("Consolas", 20), fg = "black").place(x=50,y=70)
        Label(root, text = "Choose a gamemode", font=("Consolas", 10), fg = "black").place(x=50,y=120)
        Label(root, text = "to the right.", font=("Consolas", 10), fg = "black").place(x=60,y=140)

        Label(root, text = "Instructions", font=("Consolas", 20), fg = "black").place(x=30,y=250)
        Label(root, text = "How to Play", font=("Consolas", 13), fg = "black").place(x=30,y=285)
        Label(root, text = "Wordle is a puzzle game that allows the users to puzzle", font=("Consolas", 8), fg = "black").place(x=30,y=320)
        Label(root, text = "out what the randomly chosen word is. The word has a certain", font=("Consolas", 8), fg = "black").place(x=22,y=340)
        Label(root, text = "number of letters, depending on the gamemode chosen. The", font=("Consolas", 8), fg = "black").place(x=30,y=360)
        Label(root, text = "EASY gamemode makes the user guess 4-letter words. The MEDIUM", font=("Consolas", 8), fg = "black").place(x=22,y=380)
        Label(root, text = "gamemode makes the user guess 5-letter words, and the HARD", font=("Consolas", 8), fg = "black").place(x=28,y=400)
        Label(root, text = "mode, 6-letter words. Once a difficulty is chosen, the user", font=("Consolas", 8), fg = "black").place(x=22,y=420)
        Label(root, text = "could start guessing the word. The correctly inputted letters", font=("Consolas", 8), fg = "black").place(x=22,y=440)
        Label(root, text = "turn green, the letters that are in the wrong place but", font=("Consolas", 8), fg = "black").place(x=30,y=460)
        Label(root, text = "somewhere in the word turn yellow, and the completely wrong", font=("Consolas", 8), fg = "black").place(x=22,y=480)
        Label(root, text = "letters turn gray. Try your best to guess the word, have fun!", font=("Consolas", 8), fg = "black").place(x=22,y=500)
        canvas.create_line(2, 27, 500, 27, width=2)
        canvas.create_line(2, 230, 500, 230, width=2)

        canvas.create_line(2, 22, 500, 22, dash=(7), width=2)
        canvas.create_line(2, 235, 500, 235, dash=(7), width=2)
        canvas.pack()
    def setup_easy(self):
        pass

    def setup_intermediate(self):
        pass

    def setup_hard(self):
        pass

    def setup_shop(self):
        pass

root = Tk() 
root.title("Homepage")
root.geometry("400x600")
app = Application(root)
root.mainloop()