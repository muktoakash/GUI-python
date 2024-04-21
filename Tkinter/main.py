"""./random_wprds.py

GUI App using PyQt5 that choses random words to display from
the nltk.corpus at the press of buttons.
"""

# Import Modules
from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

# imports to use for words
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary

# global constant:
NUM_RANDOM_WORDS = 3 # currently only choosing three random words

# Main App Objects and Settings
app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(300, 200)

# Create all App Objects
title_text = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")

# Use all words in nltk corpus with a meaning
word_list = list(word for word in wn.words() if word.isalpha())

# All Design Here
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Getting a Random Word from a List
random_words = list(range(NUM_RANDOM_WORDS))

# Getting a Random Word from a List
def random_word(btn):
    """
    Chooses a random word to append to random_words
    side-effect: Modifies random_words
    """
    word = choice(word_list)
    while word in random_words:
        word = choice(word_list)
    random_words[btn] = word

# Events
button1.clicked.connect(lambda: (random_word(0),
                         text1.setText(random_words[0])))
button2.clicked.connect(lambda: (random_word(1),
                         text2.setText(random_words[1])))
button3.clicked.connect(lambda: (random_word(2),
                         text3.setText(random_words[2])))

# Show/Run our App
main_window.show()
app.exec_()
