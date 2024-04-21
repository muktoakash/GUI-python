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

# Class for main app
class RandomWords():
    """
    Creates a Tk() object to play the game.
    """
    def __init__(self):
        """Initialize"""
        # Main App Objects and Settings
        self.root = Tk()

        # Title
        self.root.title("Vocab Show Down!")

        # Use all words in nltk corpus with a meaning
        self.word_list = list(word for word in wn.words() if word.isalpha())

        # Create all App Objects
        self.text1 = Label(self.root, text="?", height=2, width=30, relief="raised")
        self.text2 = Label(self.root, text="?", height=2, width=30, relief="raised")
        self.text3 = Label(self.root, text="?", height=2, width=30, relief="raised")

        self.random_words = [self.text1, self.text2, self.text3]

        # Widgets
        self.button = Button(self.root, text="Get New Random Words!", command = self.random_word)

        # Layout
        self.button.grid(row=0, column=1)
        for index in range(NUM_RANDOM_WORDS):
            self.random_words[index].grid(row = 1, column = index)
        # self.text1.grid(row=1, column=0)
        # self.text2.grid(row=1, column=1)
        # self.text3.grid(row=1, column=2)

    # Getting Random Words
    def random_word(self):
        """
        Chooses a random word to append to random_words
        side-effect: Modifies random_words
        """
        for index in range(NUM_RANDOM_WORDS):
            current_words = [self.random_words[i]["text"] \
                              for i in range(NUM_RANDOM_WORDS)]
            word = choice(self.word_list)
            while word in current_words:
                word = choice(word_list)
            self.random_words[index].configure(text =word)


# Show/Run our App
if __name__== "__main__":
    app = RandomWords()
    app.root.mainloop()
