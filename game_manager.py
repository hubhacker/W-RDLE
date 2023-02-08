from tkinter import *

class GameManager (object):
    def __init__(self):
        self.root = Tk()
        self.screen = None

    def home_screen (self):
        self.root.title ("Select game mode:")
        self.difficulties = Difficulties ("difficulty.txt")