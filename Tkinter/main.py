"""./Demo_App.py

Simple dempnstration of Tkinter set up.
"""

# imports
from tkinter import Tk, Label, Entry, Button, StringVar, Text, END

class DemoApp():
    """Simple app to demonstrate tkinter GUI set up.
    
    Attributes:
    - open_program  : Tkinter root
    - entry_soft    : StringVar
    - entry         : Text
    - button        : Button
    
    Methods:
    private:
        read_file()
        on_click(event)
    """

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

        # self.message = Label(self.open_program, text="Welcome to the Demo App")
        # Input
        self.entry_soft = StringVar()       # Creates a Tkinter StringVar object 
                                            # to hold data for an Entry widget.
        # TextBox
        self.text = Text(self.open_program, height=2, width=23)   # Creates a Text widget
                                                        # with specified height and width.
        # Button
        self.button = Button(self.open_program, text="Copy Me!", command=self.read_file)


        # Initialize entry
        self.entry = Entry(self.open_program, textvariable=self.entry_soft)    
                                                                # Creates an Entry widget 
                                                                # that will display/edit 
                                                                # the text in entry_soft.
        self.entry.config(foreground='gray')
        self.entry.bind("<Button-1>", self.on_click)            # Clear default on click
        self.entry.bind("<FocusIn>", self.on_click)             # Or in Focus

        # Layout
        """
        Tkinter has two main ways to organize widgets within the window — .pack() and .grid().

        .pack() stacks widgets vertically or horizontally in the window.

        .grid() positions widgets in a tabular grid format by specifying rows and columns.
        """
        self.entry_soft.set("Enter Number")
        self.entry.grid(row=0, column=0) # align the label and input side-by-side
        self.text.grid(row=1, column=0)  # creates an Entry box and a Text box
                                    # side by side in the first row of the GUI

        #b1.pack() " this is one way to execute a button
        self.button.grid(row = 0, column = 1) #gives us more control


    # functionality (responding to events)
    def read_file(self):
        """Reads and appends the value from text box."""
        try:
            self.text.delete("1.0", "end") # clear text box
            value = float(self.entry_soft.get()) # .get() retrieves the content of a widget
            self.text.insert(END, value) #alue of text would be inputted at the END and 
                                #also takes the value of entry_soft
            self.entry.delete(0, END)
        except ValueError:
            value = "Please insert a number above"
            self.text.insert(END, value) #alue of text would be inputted at the END and 
                                #also takes the value of entry_soft
            self.entry.delete(0, END)
    
    def on_click(self, event):
        """Clears default value for entry"""

        self.entry.config(foreground='black')
        if self.entry.get() == "Enter Number":
            event.widget.delete(0, END)
        else:
            self.entry.config(foreground='black')

# Run
if __name__ == "__main__":
    demo = DemoApp()
    demo.open_program.mainloop()