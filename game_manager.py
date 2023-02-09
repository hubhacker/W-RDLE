from tkinter import *

from homepage import Application
from easy_gamemode import Easy
from intermediate_gamemode import Intermediate
from hard_gamemode import Hard

class GameManager (object):
    def __init__(self):
        self.root = Tk()
        self.screen = None


    def setup_homescreen (self):
        self.root.title ("Select game mode:")
        self.screen = Application(self, master= self.root
                                  callback_hompage = self.onclose_homepage)
    def onclose_homepage(self):
        self.screen.destroy()
        self.screen= Easy(master = self.root, )
        

def main():
    game = GameManager()
    game.setup_homescreen()
    game.root.mainloop()
main()