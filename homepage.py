from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self, text = "W ♾ RDLE", font=("Helvetica", 20),
            width=20, fg = "green").grid(row=0, column=1, columnspan = 1, sticky=W+E)
        
        Label(self, text= "Easy Mode!", font = "Century 13" , fg = "HotPink3").grid(row = 2, column = 1, )
        Button()

        Label(self, text = "Intermediate Mode!", font = "Century 13", fg = "DarkOrchid2").grid(row = 2, column = 4)
        Button()

        Label(self, text= "Hard Mode!", font = "Century 13", fg = "PeachPuff4").grid(row = 2, column = 7)
        Button()
        
root = Tk()
root.title("Homepage")
app = Application(root)
root.mainloop()


