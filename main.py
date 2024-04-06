# Import Modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QLineEdit, QComboBox, QDateEdit, QTableWidget, \
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# App Class
class ExpenseApp(QWidget):
    """
    """
    def __init__(self):
        super().__init__()
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

    # Create Objects

    # Design App with Layouts
        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.row1.addWidget(QLabel("Date:"))
        self.row1.addWidget(self.date_box)
        self.row1.addWidget(QLabel("Category:"))
        self.row1.addWidget(self.dropdown)

        self.row2.addWidget(QLabel("Amount:"))
        self.row2.addWidget(self.amount)
        self.row2.addWidget(QLabel("Description:"))
        self.row2.addWidget(self.description)

        self.row3.addWidget(self.add_button)
        self.row3.addWidget(self.delete_button)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)

        self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)

# Create Database
database = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName("expense.db")
if not database.open():
    QMessageBox.critical(None, "Error", "Could not open Database")
    sys.exit(1)

query = QSqlQuery()
query.exec_("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
            """)

# Run the App
if __name__ in "__main__":
    app = QApplication([])
    main = ExpenseApp()
    main.show()
    app.exec_()
