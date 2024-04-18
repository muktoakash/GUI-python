"""./Demo_App.py"""
# imports
from tkinter import Tk, Label, Entry, Button, StringVar, Text, mainloop

class DemoApp():
    """Simple app to demonstrate tkinter GUI set up."""

    def __init__(self):
        """Initialize the app with root and widgets"""

        """
        TK() allows opeing a graphical interface, otherwise the program closes.
        It creates the root window, which is assigned to open_program.
        """
        self.open_program = Tk()

        # Title
        self.open_program.title("Demo Tkinter App")

        # Widgets

        self.message = Label(root, text="Welcome to the Demo App")
        # Input
        self.entry_soft = StringVar()    # Creates a Tkinter StringVar object 
                                    # to hold data for an Entry widget.
        self.entry = Entry(self.open_program, textvariable=self.entry_soft)    # Creates an Entry widget 
                                                                # that will display/edit 
                                                                # the text in entry_soft.
        # Button
        self.button = Button(self.open_program, text="Click Me!", command=self.read_file)
        # TextBox
        self.text = Text(self.open_program, height=2, width=23)   # Creates a Text widget
                                                        # with specified height and width.


        # Layout
        """
        Tkinter has two main ways to organize widgets within the window — .pack() and .grid().

        .pack() stacks widgets vertically or horizontally in the window.

        .grid() positions widgets in a tabular grid format by specifying rows and columns.
        """
        self.message.pack()
        self.entry.grid(row=0, column=1) # align the label and input side-by-side
        self.text.grid(row=0, column=2)  # creates an Entry box and a Text box
                                    # side by side in the first row of the GUI

        #b1.pack() " this is one way to execute a button
        self.button.grid(row = 0, column = 0) #gives us more control


    # functionality (responding to events)
    def read_file(self):
        """Reads and appends the value from text box."""
        value = float(self.entry_soft.get()) # .get() retrieves the content of a widget
        self.text.insert(END, value) #alue of text would be inputted at the END and 
                                #also takes the value of entry_soft

# Run
if __name__ == "__main__":
    demo = DemoApp()
    demo.open_program.mainloop()