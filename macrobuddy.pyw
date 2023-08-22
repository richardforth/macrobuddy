# KeyboardPal
# Type out user input automatically after 5 seconds

from tkinter import *
from tkinter import scrolledtext
import pyautogui
import time

### Configuration Options
TYPING_SPEED  = 0.02 # 0.02 feels like a natural typing speed. hence default
NEWLINE_DELAY = 1.2  # additional delay for any newlines, to stop screwups


class Application(Frame):
    """ GUI application that acts like a 9-key macro keyboard. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        #self.grid()
        self.grid(row=0, column=0, sticky = "nsew")
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label
        Label(self,
              text = "Macro starts after 5 seconds"
              ).grid(row = 0, column = 0, columnspan = 3, sticky = "nsew")

        # Buttons Row 1
        Button(self,
               text = "1",
               command = self.macro1
               ).grid(row = 1, column = 0, sticky = "nsew")

        Button(self,
               text = "2",
               command = self.macro2
               ).grid(row = 1, column = 1, sticky = "nsew")

        Button(self,
               text = "3",
               command = self.macro3
               ).grid(row = 1, column = 2, sticky = "nsew")

        # Buttons Row 2
        Button(self,
               text = "4",
               command = self.macro4
               ).grid(row = 2, column = 0, sticky = "nsew")

        Button(self,
               text = "5",
               command = self.macro5
               ).grid(row = 2, column = 1, sticky = "nsew")

        Button(self,
               text = "6",
               command = self.macro6
               ).grid(row = 2, column = 2, sticky = "nsew")

        # Buttons Row 3
        Button(self,
               text = "7",
               command = self.macro7
               ).grid(row = 3, column = 0, sticky = "nsew")

        Button(self,
               text = "8",
               command = self.macro2
               ).grid(row = 3, column = 1, sticky = "nsew")

        Button(self,
               text = "9",
               command = self.macro3
               ).grid(row = 3, column = 2, sticky = "nsew")


        ## required for flexible window resizing
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)



    def typit(self, text):
        """ Types the text in the box. """
        # get values from the GUI
        myText = text
        lines = myText.splitlines()
        time.sleep(5) 
        self.typout(lines)
        # https://github.com/asweigart/pyautogui/issues/46#issuecomment-132640299


    def typout(self, lines):
        for line in lines:
            ## skip last newline
            ## Only provide newlines "between" lines
            if (line == lines[-1]):
                pyautogui.typewrite(line, TYPING_SPEED)
            else:
                pyautogui.typewrite(line, TYPING_SPEED)
                pyautogui.typewrite("\n")
                time.sleep(NEWLINE_DELAY)

    ### MODIFY/EDIT MACROS HERE USING PYTHON CODE/PYAUTOGUI KEY COMBINATIONS 
    def macro1(self):
        """ Type a simple message in any active editor "Hello World!" """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        message="Hello World!"
        self.typit(message)

    def macro2(self):
        """ Type a multi line string into any active editor """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        message="""Mary had a little lamb,
whose fleece was white as snow.

And everywhere that Mary went,
the lamb was sure to go.

It followed her to school one day
which was against the rules.

It made the children laugh and play,
to see a lamb at school.

And so the teacher turned it out,
but still it lingered near,

And waited patiently about,
till Mary did appear.

“Why does the lamb love Mary so?”
the eager children cry.

“Why, Mary loves the lamb, you know.”
the teacher did reply. """
        self.typit(message)

    def macro3(self):
        """ Brief description of macro """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        pass

    def macro4(self):
        """ Brief description of macro """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        pass

    def macro5(self):
        """ Brief description of macro """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        pass

    def macro6(self):
        """ Brief description of macro """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        pass

    def macro7(self):
        """ Brief description of macro """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        pass

    def macro8(self):
        """ Brief description of macro """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        pass

    def macro9(self):
        """ Brief description of macro """
        time.sleep(5) # Leave this line as it creates the 5 second delay
        pass
 

# main
root = Tk()
root.title("MacroBuddy")
app = Application(root)
root.geometry("600x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.attributes('-topmost',True)
root.mainloop()
