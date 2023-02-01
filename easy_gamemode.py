from tkinter import *
import random

class Application(Frame):

    def __init__(self,master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def choose_word(self,file):

        file=open("midyear_4letterwords.txt")
        