from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def choose_word(self, file): 
        sixletter = open(file)

        self.sixletterlist = []

        for word in sixletter:
            self.sixletterlist.append(word.strip())

        self.word = self.sixletterlist([random.randint(0, 1000)])


