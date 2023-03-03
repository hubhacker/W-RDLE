from tkinter import *

from homepage import Application
from easy_gamemode import Easy
from intermediate_gamemode import Intermediate
from hard_gamemode import Hard

class GameManager(object):

    def __init__(self):
        
        self.root = tkinter.Tk()
        self.current_screen = None

    def setup_homescreen(self):
        self.root.title("Select Game Mode:")
        self.screen = Application(self, master= self.root, callback_hompage = self.onclose_homepage)
        self.screen = GameManager(self, master= self.root, callback_homepage = self.onclose_homepage)

    def onclose_homepage(self):
        self.screen.destroy()
        self.screen = Easy(self, master= self.root, callback_easy= self.onclose_easy)
        

#def main():
    #game = GameManager()
    #game.setup_homescreen()
    #game.root.mainloop()
#main()