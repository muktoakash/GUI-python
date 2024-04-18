"""./Demo_App.py"""
# imports
from tkinter import Tk, Label, Entry, Button, StringVar, Text, mainloop

"""
TK() allows opeing a graphical interface, otherwise the program closes.
It creates the root window, which is assigned to open_program.
"""
open_program = Tk()

# Title
root.title("Demo Tkinter App")

# Widgets


message = Label(root, text="Welcome to the Demo App")
# Input
entry_soft = StringVar()    # Creates a Tkinter StringVar object 
                            # to hold data for an Entry widget.
entry = Entry(open_program, textvariable=entry_soft)    # Creates an Entry widget 
                                                        # that will display/edit 
                                                        # the text in entry_soft.
# Button
button = Button(open_program, text="Click Me!", command=read_file)
# TextBox
text = Text(open_program, height=2, width=23)   # Creates a Text widget
                                                # with specified height and width.


# Layout
"""
Tkinter has two main ways to organize widgets within the window — .pack() and .grid().

.pack() stacks widgets vertically or horizontally in the window.

.grid() positions widgets in a tabular grid format by specifying rows and columns.
"""
message.pack()
entry.grid(row=0, column=1) # align the label and input side-by-side
text.grid(row=0, column=2)  # creates an Entry box and a Text box
                            # side by side in the first row of the GUI

#b1.pack() " this is one way to execute a button
button.grid(row = 0, column = 0) #gives us more control


# functionality (responding to events)
def read_file():
    value = float(entry_soft.get()) # .get() retrieves the content of a widget
    text.insert(END, value) #alue of text would be inputted at the END and 
                            #also takes the value of entry_soft

# Run
open_program.mainloop()