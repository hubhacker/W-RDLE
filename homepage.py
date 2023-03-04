from tkinter import *

#from easy_gamemode import Application
#from intermediate_gamemode import Application
#from hard_gamemode import Application
#from shop import Application

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.easy_screen = None
        self.intermediate_screen = None
        self.hard_screen = None
        self.shop_screen = None
        #self.callback_on_easy = callback_on_easy
        
    def create_widgets(self):
        canvas = Canvas()

        
        Label(root, text = "W♾RDLE", font=("Consolas", 30), fg = "black").place(x=110,y=10)
        
        #Label(self, text= "Easy Mode!", font = "Century 13" , fg = "HotPink3").grid(row = 5, column = 1)
        Button(root, text = " EASY ", command = self.setup_easy, font =("Consolas", 15), fg = "black", bg = "#F9DCC4", width=13, height=1).place(x=220,y=65)

        # #Label(self, text = "Intermediate Mode!", font = "Century 13", fg = "DarkOrchid2").grid(row = 5, column = 2)
        Button(root, text = "MEDIUM", command = self.setup_intermediate, font =("Consolas", 15), fg = "white", bg= "#CDB4DB", width=13, height=1).place(x=220, y=115)

        # #Label(self, text= "Hard Mode!", font = "Century 13", fg = "PeachPuff4").grid(row = 5, column = 3)
        Button(root, text = " HARD ", command = self.setup_hard, font =("Consolas", 15), fg = "white", bg = "#4f7aa8", width=13, height=1).place(x=220,y=165)

        canvas.create_line(2, 27, 500, 27, width=2)
        canvas.create_line(2, 230, 500, 230, width=2)
        canvas.create_line(2, 22, 500, 22, dash=(7), width=2)
        canvas.create_line(2, 235, 500, 235, dash=(7), width=2)
        canvas.pack()

    def setup_easy(self):
        pass

    def setup_intermediate(self):
        pass

    def setup_hard(self):
        pass

    def setup_shop(self):
        pass
        
root = Tk() 
root.title("Homepage")
root.geometry("400x600")
app = Application(root)
root.mainloop()