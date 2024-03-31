"""./main.py"""

# Import Modules
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, \
    QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(900, 700)

# All app widgets/objects
btn_folder = QPushButton("Folder")
file_list = QListWidget()

btn_orig = QPushButton("Original")
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpen")
gray = QPushButton("Black/White")
saturation = QPushButton("Color")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

# Transformations
transformations = {
            "B/W" : lambda image: image.convert("L"),
            "Color" : lambda image: ImageEnhance.Color(image).enhance(1.2),
            "Contrast" : lambda image: ImageEnhance.contrast(image).enhance(1.2),
            "Blur" : lambda image: image.filter(ImageFilter.BLUR),
            "Left" : lambda image: image.transpose(Image.ROTATE_90),
            "Right" : lambda image: image.transpose(Image.ROTATE_270),
            "Mirror" : lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
            "Sharpen" : lambda image: image.filter(ImageFilter.SHARPEN),
        }

# Widget List
widgets = [btn_folder,
    file_list,
    btn_left,
    btn_right,
    mirror,
    sharpness,
    gray,
    saturation,
    contrast,
    blur]

# Label list
labels = ["Original",
    "Left",
    "Right",
    "Mirror",
    "Sharpen",
    "Black/White",
    "Color",
    "Contrast",
    "Blur"]

# Dropdown box
filter_box = QComboBox()

# Generate Filer Boxes
for label in labels:
    filter_box.addItem(label)

picture_box = QLabel("Image will appear here!")

# App Design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

for widget in widgets:
    col1.addWidget(widget)

col2.addWidget(picture_box)

# Set the layout in a 20-80 split
master_layout.addLayout(col1, 20)
master_layout.addLayout(col2, 80)

main_window.setLayout(master_layout)

# All app functionality
working_directory = ""

# filter files and extensions
def filter(files, extensions):
    results = list()

    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)

    return results

# choose current work directory
def getWorkDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = ['.jpg', '.jpeg', '.png', '.svg']
    filenames = filter(os.listdir(working_directory), extensions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)

class Editor():

    def __init__(self, transformations = transformations) -> None:
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"
        self.transformations = transformations

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_directory, self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_image(self):
        path = os.path.join(working_directory, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        picture_box.hide()
        image = QPixmap(path)
        w, h = picture_box.width(), picture_box.height()
        image = image.scaled(w, h, Qt.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()

    # Editing Methods:
    def transformImage(self, transformation):

        transform_function = self.transformations.get(transformation)
        if transform_function:
            self.image = transform_function(self.image)
            self.save_image()

        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def apply_filter(self, filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            filter_function = self.transformations.get(filter_name)
            if filter_function:
                self.image = filter_function(self.image)
                self.save_image()
                image_path = os.path.join(working_directory, self.save_folder, self.filename)
                self.show_image(image_path)
            pass

        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder,
                                self.filename)
        self.show_image(image_path)

def handle_filter():
    if file_list.currentRow() >= 0:
        select_filter = filter_box.currentText()
        main.apply_filter(select_filter)


def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main.load_image(filename)
        main.show_image(os.path.join(working_directory, main.filename))

main = Editor()

btn_folder.clicked.connect(getWorkDirectory)
file_list.currentRowChanged.connect(displayImage)
filter_box.currentTextChanged.connect(handle_filter)

gray.clicked.connect(lambda: main.transformImage("B/W"))
btn_left.clicked.connect(lambda: main.transformImage("Left"))
btn_right.clicked.connect(lambda: main.transformImage("Right"))
sharpness.clicked.connect(lambda: main.transformImage("Sharpen"))
saturation.clicked.connect(lambda: main.transformImage("Color"))
contrast.clicked.connect(lambda: main.transformImage("Contrast"))
blur.clicked.connect(lambda: main.transformImage("Blur"))
mirror.clicked.connect(lambda: main.transformImage("Mirror"))

# show
main_window.show()
app.exec_()
# """
