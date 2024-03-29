from tkinter import *
import tkinter
from easy_gamemode import Easy
from intermediate_gamemode import Intermediate
from hard_gamemode import Hard
from shop import Shop

class GameManager(object):

    def __init__(self):
        
        self.root = tkinter.Tk()
        self.current_screen = None

    def setup_homescreen(self):
        self.root.title("Select Game Mode")
        self.current_screen = Application(self, master= self.root, callback_hompage = self.onclose_homepage)
        self.current_screen = GameManager(self, master= self.root, callback_homepage = self.onclose_homepage)

    def onclose_easy(self): 
        self.current_screen.destroy()
        self.root.title("Easy Mode!")
        self.current_screen = Easy(self, master = self.root, callback_easy = self.onclose_easy)

    def onclose_intermediate(self):
        self.current_screen.destroy()
        self.root.title("Intermediate Mode!")
        self.current_screen = Intermediate(self, master = self.root, callback_intermediate = self.onclose_intermediate)

    def onclose_hard(self):
        self.current_screen.destroy()
        self.root.title("Hard Mode!")
        self.current_screen = Hard(self, master = self.root, callback_hard = self.onclose_hard)

    def onclose_shop(self):
        self.current_screen.destroy()
        self.root.title("Shop")
        self.current_screen = Shop(self, master = self.root, callback_shop = self.onclose_shop)
        

#def main():
    #game = GameManager()
    #game.setup_homescreen()
    #game.root.mainloop()
#main()