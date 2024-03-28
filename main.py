"""./main.py"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(900, 700)


main_window.show()
app.exec_()
