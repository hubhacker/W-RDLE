from tkinter import *
# import it

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
# create the things first




















    def create_widgets(self):
        Label(self, text = "Enter information for a new story").grid(row=0, column=0, columnspan = 2, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column =1, sticky = W)

        Label(self, text = "Person: ").grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        Label(self, text="Silly word: ").grid(row=2,column=0,sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column= 1, sticky = W)


        Label(self, text="Adjective(s):").grid(row=4, column=0, sticky=W)

        self.is_achy = BooleanVar()
        Checkbutton(self, text = "achy", variable = self.is_achy).grid(row=4, column=1, sticky=W)

        self.is_woozy = BooleanVar()
        Checkbutton(self, text="woozy", variable=self.is_woozy).grid(row=4, column=2, sticky=W)

        self.is_dizzy = BooleanVar()
        Checkbutton(self, text="dizzy", variable = self.is_dizzy).grid(row=4, column=3, sticky=W)
# use specific types of buttons or radio whatever because that changes the number of selectable options
        Label(self, text = "Body Part:").grid(row=5, column=0, sticky=W)
        self.body_part = StringVar()
        self.body_part.set(None)

        Label(self, text = "Time:").grid(row=6, column=0, sticky=W)
        self.time = StringVar()
        self.time.set(None)
        time = ["days", "weeks", "months", "years"]
        column = 1
        for part in time:
            Radiobutton(self, text=part, variable=self.time,value=part).grid(row=6, column=column, sticky =W)
            column+=1

        body_parts = ["stomach", "lungs", "ribcage"]
        column = 1
        for part in body_parts:
            Radiobutton(self, text=part, variable=self.body_part,value=part).grid(row=5, column=column, sticky =W)
            column+=1
        Button(self, text = "Click for story", command=self.tell_story).grid(row=7, column=0, sticky=W)

        self.story_txt = Text(self, width=75, height=10, wrap = WORD)
        self.story_txt.grid(row = 8, column=0, columnspan=5)

    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        adjectives = ""
        if self.is_achy.get():
            adjectives += "achy, "
        if self.is_woozy.get():
            adjectives += "woozy, "
        if self.is_dizzy.get():
            adjectives += "dizzy, "
        body_part = self.body_part.get()
        time = self.time.get()
# print the entire story
        story = "Hello, my child "
        story += person + ""
        story += " will not be attending school today- they got an awful case of the "
        story += noun.title() + ""
        story += " disease. "
        story += person + " "
        story += "tested positive for"
        story += " " + noun + ""
        story += " disease a few days ago, and she's been feeling "
        story += adjectives
        story += "all day!  "
        story += "These symptoms have been especially extreme in " 
        story += person + "'s "
        story += body_part + ". "
        story += "Overall, "
        story += person + " "
        story += "should be back in school in a few"
        story += " " + time + ". "
        story += "Thank you for understanding!   -"
        story += person + "'s "
        story += "mother"
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()