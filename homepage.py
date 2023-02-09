from tkinter import *

from easy_gamemode import Application
from intermediate_gamemode import Application
from hard_gamemode import Application
from shop import Application

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.easy_screen = None
        self.intermediate_screen = None
        self.hard_screen = None
        self.shop_screen = None
        
        
    def create_widgets(self):
        Label(self, text = "W ♾ RDLE", font=("Helvetica", 60),
            width=20, fg = "green").grid(row=0, column=1, columnspan = 1, sticky=N)
        
        #Label(self, text= "Easy Mode!", font = "Century 13" , fg = "HotPink3").grid(row = 5, column = 1)
        Button(self, text = "Easy Mode!", command = self., font =, fg = ).grid(row = , column = , sticky = )

        #Label(self, text = "Intermediate Mode!", font = "Century 13", fg = "DarkOrchid2").grid(row = 5, column = 2)
        Button(self, text = "Intermediate Mode!", command = self., font =, fg = ).grid(row = , column = , sticky = )

        #Label(self, text= "Hard Mode!", font = "Century 13", fg = "PeachPuff4").grid(row = 5, column = 3)
        Button(self, text = "Hard Mode!", command = self., font =, fg = ).grid(row = , column = , sticky = )


    def setup_easy(self):
        # changes the window's title
        root.title ("Easy Mode!")

        self.easy_screen = Application(master = root, )

    def setup_intermediate(self):
        pass

    def setup_hard(self):
        pass

    def setup_shop(self):
        pass
        
root = Tk() 
root.title("Homepage")
app = Application(root)
root.mainloop()
