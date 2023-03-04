from tkinter import *

from easy_gamemode import Application
from intermediate_gamemode import Application
from hard_gamemode import Application
from shop import Application
from game_manager import GameManager

class Application(Frame):
    def __init__(self, master):
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