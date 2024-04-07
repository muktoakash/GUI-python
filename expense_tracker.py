"""./expense_tracker.py

    GUI App to keep track of day-to-day expenses.
"""

# Import Modules
import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QLineEdit, QComboBox, QDateEdit, QTableWidget, QTableWidgetItem, \
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QHeaderView
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# App Class
class ExpenseApp(QWidget):
    """
    ExpenseApp()

    Attributes:
    - date_box
    - dropdown : for expense category
    - amount
    - description
    - table : for displaying database entries

    Methods:
    - load_table()
    - add_expense()
    - delete_expense()
    """

    def __init__(self):
        super().__init__()

    #Main App Objects & Settings
        self.resize(550, 500)
        self.setWindowTitle("Expense Tracker")

        # Attributes
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        # Buttons
        self.add_button = QPushButton("Add Expenses")
        self.add_button.clicked.connect(self.add_expense)
        self.delete_button = QPushButton("Delete Expenses")
        self.delete_button.clicked.connect(self.delete_expense)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5) # ID, date, category, amount, description
        self.header_names = ['Id', 'date', 'Category', 'Amount', 'Description']
        self.table.setHorizontalHeaderLabels(self.header_names)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.sortByColumn(1, Qt.DescendingOrder)

    # Design App with Layouts

        # CSS stylesheet
        self.setStyleSheet("""
                           QWidget {background-color: #b8c9e1;}

                           QLabel{
                            color: #333;
                            font-size: 14px;
                           }

                           QLineEdit, QComboBox, QDateEdit {
                            background-color: #b8c9e1;
                            color: #333;
                            border: 1px solid #444;
                            padding: 5px;
                           }

                           QTableWidget {
                            background-color: #b8c9e1;
                            color: #333;
                            border: 1px solid #444;
                            selection-background-color: #ddd;
                           }

                           QPushButton {
                            background-color: #4caf50;
                            color: #fff;
                            border: none;
                            padding: 8px 16px;
                            font-size: 14px;
                           }

                           QPushButton:hover {
                            background-color: #45a049;
                           }

                           """)

        # Create categories for dropdown
        categories = ['Food', 'Transportaion', 'Rent', 'Shopping', 'Entertainment', 'Bills', 'Other']
        self.dropdown.addItems(categories)

        # Layout
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
        """load_table()

        Loads the database table for display
        """
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

        # Sort the table by date
        self.table.sortByColumn(1, Qt.DescendingOrder)

    def add_expense(self):
        """add_expense()

        Functionality to add expense to the database.
        Connected to self.add_button
        """

        # Gather data from attributes
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        # Create and execute SQL query
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

        # Clean up
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

        self.load_table()

    def delete_expense(self):
        """delete_expense()

        Deletes selected expense row from the database.
        Connected to self.delete__button
        """

        # Select a row
        selected_row = self.table.currentRow()

        # Error handling
        if selected_row == -1:
            QMessageBox.warning(self, "No Expense Chosen", "Please choose an expense to delete!")
            return

        # Get Id for SQL
        expense_id = int(self.table.item(selected_row, 0).text())

        # Confirmation
        confirm = QMessageBox.question(self, "Are you sure?", "Delete Expense?", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.No:
            return

        # Create and execute SQL query
        query = QSqlQuery()
        query.prepare("DELETE FROM expenses WHERE id = ?")
        query.addBindValue(expense_id)
        query.exec_()

        self.load_table()

# Create Database
database = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName("expense.db")
if not database.open():
    QMessageBox.critical(None, "Error", "Could not open Database")
    sys.exit(1)

# Create and execute SQL query
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
