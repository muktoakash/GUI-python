"""./random_wprds.py

GUI App using PyQt5 that choses random words to display from
the nltk.corpus at the press of buttons.
"""

# Import Modules
from random import choice

# imports
from tkinter import Tk, Entry, Button, StringVar, Text, Label, END

# imports to use for words
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary

# global constant:
NUM_RANDOM_WORDS = 3 # currently only choosing three random words

# Main App Objects and Settings
root = Tk()

# Title
root.title("Vocab Show Down!")

# Functionalities:

# Create all App Objects
text1 = Label(root, text="?", height=2, width=30, relief="raised")
text2 = Label(root, text="?", height=2, width=30, relief="raised")
text3 = Label(root, text="?", height=2, width=30, relief="raised")

# Use all words in nltk corpus with a meaning
word_list = list(word for word in wn.words() if word.isalpha())

# Getting a Random Word from a List
random_words = [text1, text2, text3]
# Getting Random Words
def random_word():
    """
    Chooses a random word to append to random_words
    side-effect: Modifies random_words
    """
    for index in range(NUM_RANDOM_WORDS):
        word = choice(word_list)
        while word in random_words:
            word = choice(word_list)
        random_words[index].configure(text =word)


# Widgets
button = Button(root, text="Get New Random Words!", command = random_word)

# All Design Here
button.grid(row=0, column=1)
text1.grid(row=1, column=0)
text2.grid(row=1, column=1)
text3.grid(row=1, column=2)


# Events


# Show/Run our App

root.mainloop()
