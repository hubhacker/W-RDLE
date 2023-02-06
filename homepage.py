from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self, text = "W ♾ RDLE", font=("Helvetica", 20),
            width=20, fg = "green").grid(row=0, column=1, columnspan = 1, sticky=W+E)
        
        Label(self, text= "Easy Mode", font = "Century 13" , fg = ).grid()
        Label(self, text = "Intermediate Mode", font = "Century 13", fg = ).grid()
        Label(self, text= "Hard Mode", font = "Century 13", fg =).grid()

        
root = Tk()
root.title("Homepage")
app = Application(root)
root.mainloop()


