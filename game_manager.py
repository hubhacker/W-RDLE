from tkinter import *

from homepage import Application

class GameManager (object):
    def __init__(self):
        self.root = Tk()
        self.screen = None

    def setup_homescreen (self):
        self.root.title ("Select game mode:")
        self.screen = Application 
def main():
    game = GameManager()
    game.setup_homescreen()
    game.root.mainloop()
main()