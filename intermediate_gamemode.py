import tkinter
import random

class Application (Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def choose_word(self, file): 
        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.word = self.fiveletterlist([random.randint(0, 1000)])
