"""./main.py"""

# Import Modules
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(900, 700)

# All app widgets/objects
btn_folder = QPushButton("Folder")
file_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpen")
gray = QPushButton("Black/White")
saturation = QPushButton("Color")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

# Dropdown box
filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpen")
filter_box.addItem("Black/White")
filter_box.addItem("Color")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

# show 
main_window.show()
app.exec_()
