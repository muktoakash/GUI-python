# Import Modules
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QLineEdit, QComboBox, QDateEdit, QTableWidget, \
    QPushButton, QVBoxLayout, QHBoxLayout

# App Class
class ExpenseApp(QWidget):
    """
    """
    def _init__(self):
    #Main App Objects & Settings
        self.resize(550, 500)
        self.setWindowTitle("Expense Tracker")

        self.date_box = QDateEdit()
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add Expenses")
        self.delete_button = QPushButton("Delete Expenses")

        self.table = QTableWidget()
        self.table.setColumnCount(5) # ID, date, category, amount, description
        self.header_names = ['Id', 'date', 'Category', 'Amount', 'Description']
        self.table.setHorizontalHeaderLabels(self.header_names)


        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

    # Create Objects

    # Design App with Layouts

# Run the App
