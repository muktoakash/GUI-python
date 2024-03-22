"""./main.py"""

# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from random import choice
from nltk.corpus import words


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

word_list = words.words() # Use all words in nltk corpus

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
def random_word1():
    word = choice(word_list)
    text1.setText(word)

def random_word2():
    word = choice(word_list)
    text2.setText(word)

def random_word3():
    word = choice(word_list)
    text3.setText(word)

# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

# Show/Run our App
main_window.show()
app.exec_()
