from tkinter import *

from homepage import Application
from easy_gamemode import Easy
from intermediate_gamemode import Intermediate
from hard_gamemode import Hard

class GameManager(object):

    def __init__(self):
        self.place()
        self.screen = None
    
    def start(self, root):
        root.title("Select Game Mode:")
        root.geometry("750x300+0+0")
        self.screen = Application(self, master = self.root, callback_hompage = self.onclose_homepage)
        self.screen = GameManager(self, master= self.root, callback_homepage = self.onclose_homepage)


    def switch(self, root):
        self.screen.destroy()



#class GameManager (object):
    #def __init__(self):
        #self.place()
        #self.screen = None


    #def setup_homescreen (self):
        #self.root.title ("Select game mode:")
        #self.screen = Application(self, master= self.root, callback_hompage = self.onclose_homepage)
        #self.screen = GameManager(self, master= self.root, callback_homepage = self.onclose_homepage)
    #def onclose_homepage(self):
        #self.screen.destroy()
        #self.screen = Easy(self, master= self.root, callback_easy= self.onclose_easy)
        

#def main():
    #game = GameManager()
    #game.setup_homescreen()
    #game.root.mainloop()
#main()