
# change this path to where your text files are stored!
file_path = r"C:\__work\Python\tutorial\Wordle\\"

# code for drawing form in tkinter
import tkinter

# for choosing a random word to guess
import random

# this module doesn't automatically get imported - 
# we'll use it do display message boxes
import tkinter.messagebox

# the colours of the Wordle buttons
dark_grey = "#777b7d"
yellow = "#c9b458"
green = "#6aaa64"
light_grey = "#d3d6da"
white = "#ffffff"
black = "#000000"

class Button:
        
    """ drawing a button on the form """
        
    def change_colour(self,colour):

        # foreground colour depends on background
        if colour == light_grey:
            self.button.configure(bg=colour,fg=black)  
        else:
            self.button.configure(bg=colour,fg=white)  

    def get_letter(self,row:int,column:int):

        # returns the letter object for this row and column (there has to be some better way to do this than
        # using this clunky list comprehension!)
        return [x for x in self.form.letters if x.row == row and x.column == column][0]
		
    def get_word(self,row:int):

        # returns the word for this row
        letters = [x.square["text"] for x in self.form.letters if x.row == row and x.column <= 5]
        return "".join(letters)

    def colour_current_row(self,target:str,word:str,row:int):

        # This is the most complicated bit!  Duplicate letters in source or target are a problem.
        # Whenever find an exact match, replace letter in both words with a *.  For inexact matches,
        # replace both with a ?.  Can then go through and process at end.  Eg if target is OOZED and
        # you guess ROBOT, will first turn to O*ZED and R*BOT, then to ?*zed and R*B?T.

        # mark as green any letter in correct position
        new_word = ""
        new_target = ""

        for position in range(0,5):

            if word[position] == target[position]:
                new_word += "*"
                new_target += "*"
            else:
                new_word += word[position]
                new_target += target[position]

        # now go through each letter in target seeing if can find in word (this will work even if there are 
        # 100% exact matches already)
        newest_target = ""
        for position in range(0,5):

            letter = new_target[position]
            if letter != "*":

                # see if this letter is in the word guessed
                for this_postion, guess_letter in enumerate(new_word):
                    if guess_letter == letter:

                        # mark as found in word, so don't use as another guess
                        new_word = new_word[:this_postion] + "?" + new_word[this_postion+1:]
                        break

                
        # colour each letter
        for position in range(0,5):

            letter = new_word[position]            
            this_letter = self.get_letter(row,position + 1)

            if letter == "*":                        
                this_letter.change_colour(green)
            elif letter == "?":
                this_letter.change_colour(yellow)
            else:
                this_letter.change_colour(dark_grey)

        # if all letters correct, report win!
        if new_word.count("*") == 5:
            tkinter.messagebox.showinfo("Congratulations!","Congratulations on guessing the word correctly!")
        else:

            # if that was row 6, they've lost
            if row >= 6:
                tkinter.messagebox.showinfo(
                    "End of game",
                    "Out of guesses!  The word to be guessed was " + self.form.target_word.upper() + "."
                )
				
    def colour_letter_buttons(self,guesses,buttons):

        # get a list of all of the guessed letters
        guessed_letters = "".join(guesses).upper()

        # remove duplicates and make back into list
        guessed_letters = list(set(guessed_letters))

        # process each button
        for button in buttons:

            # has this letter been guessed - if not, leave as is
            if button.letter not in guessed_letters:
                continue

            # if it's been guessed but isn't in target word, colour it dark grey
            if button.letter not in self.form.target_word.upper():
                button.change_colour(dark_grey)
                continue

            # if it wasn't in the last guess, colour it back to grey (not quite sure what Wordle does with this!)
            # last_guess = guesses[-1].upper()
            # if button.letter not in last_guess:
            # 	button.change_colour(light_grey)
            # 	continue

            # was it in the correct position in any of the words?
            correct_position = self.form.target_word.find(button.letter)

            if_green = False
            for guess in guesses:
                if guess[correct_position].upper() == button.letter.upper():
                    if_green = True
                    break

            # must be yellow
            if if_green:
                button.change_colour(green)
            else:
                button.change_colour(yellow)

            continue	

    # the event-handler for the OK button
    def ok_clicked(self):
        
        # get a reference to containing letters and buttons
        # buttons = self.form.letter_buttons
        # letters = self.form.letters

        # if clicked on back button, delete last letter (if any)
        if self.letter.lower() == "back":
            if self.form.current_column > 1:

                # select the next letter, and move on one
                last_letter = self.get_letter(self.form.current_row,self.form.current_column - 1)
                last_letter.square["text"] = ""
                last_letter.change_colour(white)
                
                self.form.current_column -= 1

            # ignore back button otherwise
            return

        # if clicked on enter button, process word if on the right column
        if self.letter.lower() == "enter":
            if self.form.current_column > 5:

                # get the word for this row
                this_word = self.get_word(self.form.current_row).lower()

                # stop if this isn't one of the allowed words
                if this_word not in self.form.words:
                    tkinter.messagebox.showerror("Not a valid word","{0} isn't a valid word".format(this_word.upper()))

                    # don't process this guess!
                    return

                # colour the current row and move on to the next one
                self.colour_current_row(self.form.target_word.upper(),this_word.upper(),self.form.current_row)

                self.form.current_column = 1
                self.form.current_row += 1
                
                # add this guess to list of guesses
                self.form.guesses.append(this_word)

                # now recolour letters at bottom based on what we know now
                self.colour_letter_buttons(self.form.guesses,self.form.letter_buttons)

            return

        # if we're on column 6, nothing to do
        if self.form.current_column > 5:
            return

        # shouldn't be possible, but can't choose letters after row 6
        if self.form.current_row > 6:
            return

        # show this letter has been clicked
        # self.change_colour(dark_grey)

        # select the next letter, and move on one
        current_letter = self.get_letter(self.form.current_row,self.form.current_column)
        current_letter.square["text"] = self.letter
        current_letter.change_colour(light_grey)

        # move on to next column
        self.form.current_column += 1

    def __init__(self,form,*,left:int,top:int,width:int,letter:str):

        # name this button so can reference it
        self.id = "button_" + letter.lower()

        # the form this belongs to
        self.form = form

        # what it displays
        self.letter = letter
        
        # add a clickable button to the window (and attach event-handler for when it's clicked)
        self.button = tkinter.Button(
            form,
            text=letter,
            command=self.ok_clicked,
            width=width,
            height=2,
            relief="flat"
        )

        # colour it
        self.change_colour(light_grey)

        self.button
        self.button["padx"] = 5
        self.button["pady"] = 5

        # width and height depend on type of button
        self.button.place(x=left, y=top+370)

class Letter:

    """ each guessed letter, in  6 row x 5 column grid """
        
    def change_colour(self,colour):

        # foreground colour depends on background
        if colour == light_grey:
            self.square.configure(bg=colour,fg=black)  
        else:
            self.square.configure(bg=colour,fg=white)  

    def __init__(self,form,*,left:int,top:int,row:int,col:int):

        # remember where button is
        self.row = row
        self.column = col

        # initially it displays nothing
        self._letter = None
        
        # add this letter
        self.square = tkinter.Label(
            form,
            font=("Arial", 10, "bold"),
            text="",    #"X{0}{1}".format(row,col) ,
            width=8,
            height=4,
            borderwidth=1,
            relief="ridge",
            anchor="center"
        )

        # colour it
        self.change_colour(white)

        self.square
        # self.square["padx"] = 5
        # self.square["pady"] = 5

        # width and height depend on type of button
        self.square.place(x=left, y=top)

# create the initial window to display
def create_main_window():

    # create a window for main form of app
    wordle_form = tkinter.Tk()

    # title for dialog box
    wordle_form.title("WOW (Wise Owl Wordle)")

    # set form width and height
    form_width = 600
    form_height = 700

    # fix screen width and height
    screen_width = wordle_form.winfo_screenwidth()
    screen_height = wordle_form.winfo_screenheight()

    # calculate horizontal and vertical offset
    horizontal_offset = \
        int((screen_width/2) - (form_width/2))
    vertical_offset = \
        int((screen_height/2) - (form_height/2))

    # show form in middle of screen
    wordle_form.geometry('{0}x{1}+{2}+{3}'.format(form_width,form_height,horizontal_offset,vertical_offset))

    # stop the window being resizable
    wordle_form.resizable(False,False)

    return wordle_form

def add_letter_buttons(wordle_form):
        
    letter_buttons = []

    # add a block of buttons (5 rows, 6 columns)
    first_row = "QWERTYUIOP"
    second_row = "ASDFGHJKL"
    third_row = "ZXCVBNM"

    start_top = 130

    # first row
    start_left = 45
    for letter in first_row:
        letter_buttons.append(Button(wordle_form,left=start_left,top=start_top,width=4,letter=letter))
        start_left += 50

    # second row
    start_left = 70
    for letter in second_row:
        letter_buttons.append(Button(wordle_form,left=start_left,top=start_top + 55,width=4,letter=letter))
        start_left += 50
        
    # add the ENTER button
    letter_buttons.append(Button(wordle_form,left=50,top=start_top + 110,width=7,letter="ENTER"))

    # third row
    start_left = 120
    for letter in third_row:
        letter_buttons.append(Button(wordle_form,left=start_left,top=start_top + 110,width=4,letter=letter))
        start_left += 50

    # add the backspace button
    letter_buttons.append(Button(wordle_form,left=470,top=start_top + 110,width=7,letter="BACK"))

    # return these buttons
    return letter_buttons

def add_letters(wordle_form):
        
    letters = []

    for r in range(1,7):
        for c in range(1,6):

            # add this display letter to form
            letters.append(Letter(wordle_form,left=45 + c * 70,top= -30 + r * 70,row=r,col=c)
        )

    return letters

def get_target_word(path:str):

    words = []

    # open the text file containing targets and create words array
    with open(path + "targets.txt","r") as target_words:

        # ignore the header row
        words = target_words.read().splitlines()[1:]

    # decide what the word is
    number_words = len(words)
    word_number = random.randint(0, number_words-1)

    # get the word from the line (split by comma then unpack)
    _number, this_word = words[word_number].split(",")

    return this_word

def get_allowed_word_guesses(path:str):

    # opens text file containing possible guesses and stores them in list
    with open(path + "words.txt","r") as target_words:

        # there is no header row, so take all rows
        words = target_words.read().splitlines()

    return words

def play_game(if_debug:bool,this_target=None):

    # call function to create form to be displayed (the form and the game are synonymous, so displaying the form 
    # starts a game and closing it ends one)
    wordle_form = create_main_window()

    # add the letter buttons at the bottom
    wordle_form.letter_buttons = add_letter_buttons(wordle_form)

    # add the 6 rows of guesses (initially blank) at the top
    wordle_form.letters = add_letters(wordle_form)

    # initially on first row and first column
    wordle_form.current_row = 1
    wordle_form.current_column = 1

    # the target word (use specific one if set)
    if this_target == None:
        wordle_form.target_word = get_target_word(file_path)
    else:
        wordle_form.target_word = this_target

    if if_debug:
        print(wordle_form.target_word)

    # the (longer) list of words that a user can choose
    wordle_form.words = get_allowed_word_guesses(file_path)

    # initially there are no guesses (each is a 5-letter word)
    wordle_form.guesses = []

    # display the form
    wordle_form.mainloop() 
                
    # answer = tkinter.messagebox.askyesno(
    #     title='Another game',
    #     message='Play again?'
    # )

    # if answer:
    #     play_game()    
        
# play game (debugging writes word to guess to output window; you can override random word by setting this_target)
play_game(if_debug=False,this_target=None)



