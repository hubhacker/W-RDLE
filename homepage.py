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
        
        Label(root, text = "W ♾ RDLE", font=("Helvetica", 20), fg = "black").place(x=120,y=10)
        
        #Label(self, text= "Easy Mode!", font = "Century 13" , fg = "HotPink3").grid(row = 5, column = 1)
        Button(root, text = "Easy Mode!", command = self.setup_easy, font ="Helvetica", fg = "white", bg = "green").place(x=140,y=60)

        # #Label(self, text = "Intermediate Mode!", font = "Century 13", fg = "DarkOrchid2").grid(row = 5, column = 2)
        Button(root, text = "Intermediate Mode!", command = self.setup_intermediate, font ="Helvetica", fg = "white", bg= "blue").place(x=105, y=110)

        # #Label(self, text= "Hard Mode!", font = "Century 13", fg = "PeachPuff4").grid(row = 5, column = 3)
        Button(root, text = "Hard Mode!", command = self.setup_hard, font ="Helvetica", fg = "white", bg = "red").place(x=140,y=160)


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