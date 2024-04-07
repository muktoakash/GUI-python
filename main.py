# Import Modules
import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QLineEdit, QComboBox, QDateEdit, QTableWidget, QTableWidgetItem, \
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

        categories = ['Food', 'Transportaion', 'Rent', 'Shopping', 'Entertainment', 'Bills', 'Other']
        self.dropdown.addItems(categories)

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

        self.load_table()

    def load_table(self):
        self.table.setRowCount(0)

        query = QSqlQuery("SELECT * FROM expenses")
        row = 0
        columns = [expense_id:=None, date:=None, category:=None, amount:=None, description:=None]
        num_col = len(columns)

        while query.next():
            # Create new Table row
            self.table.insertRow(row)

            # Add values to Table
            for col_i in range(num_col):
                columns[col_i] = query.value(col_i)
                self.table.setItem(row, col_i,
                                    QTableWidgetItem(str(columns[col_i])))
            row += 1

    def add_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        query = QSqlQuery()
        query.prepare("""
                        INSERT INTO expenses (date, category, amount, description)
                        VALUES (?, ?, ?, ?)
                      """)
        query.addBindValue(date)
        query.addBindValue(category)
        query.addBindValue(amount)
        query.addBindValue(description)
        query.exec_()

        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

        self.load_table()

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
