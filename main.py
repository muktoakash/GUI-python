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

# All Design Here
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.SetLayout(master_layout)

word_list = words.words()
# Events

# Show/Run our App
main_window.show()
app.exec_()
