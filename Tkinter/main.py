# imports
from tkinter import Tk, Label, Entry, Button, StringVar, Text

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
entry_soft = StringVar()
entry = Entry(open_program, textvariable=entry_soft)
# Button
button = Button(open_program, text="Click Me!", command=read_file)
# TextBox
t1 = Text(open_program, height=2, width=23)


# Layout
"""
Tkinter has two main ways to organize widgets within the window — .pack() and .grid().

.pack() stacks widgets vertically or horizontally in the window.

.grid() positions widgets in a tabular grid format by specifying rows and columns.
"""
message.pack()
entry.grid(row=0, column=1) # align the label and input side-by-side
#b1.pack() " this is one way to execute a button
button.grid(row = 0, column = 0) #gives us more control
t1.grid(row=0, column=2)

#:
