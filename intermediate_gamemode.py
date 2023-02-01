import tkinter
import random

class Application (Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

<<<<<<< HEAD
    def split_word()
=======
    def choose_word(self, file): 
        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.word = self.fiveletterlist([random.randint(0, 1000)])
>>>>>>> d0587f58f17bb62677afd6deb7fcb72f28a3449c
