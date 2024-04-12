import os
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QTreeView, QLineEdit, QMainWindow, QLabel, QFileDialog, \
    QVBoxLayout, QHBoxLayout, QMessageBox, QCheckBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class FinanceApp(QMainWindow):
    def __init__(self):
        super(FinanceApp, self).__init__()

        self.setWindowTitle("InterestMe")
        self.resize(800, 600)

        main_window = QWidget()

        #
        self.rate_text = QLabel("Interst Rate (%):")
        self.rate_input = QLineEdit()

        self.initial_text = QLabel("Initial Investment:")
        self.initial_input = QLineEdit()

        self.years_text = QLabel("Years to Invest:")
        self.years_input = QLineEdit()

        # Creation of Our TreeView
        self.model = QStandardItemModel()
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)

        self.calc_button = QPushButton("Calculate")
        self.clear_button = QPushButton("Clear")
        self.save_button = QPushButton("Save")
        self.dark_mode = QCheckBox("Dark Mode")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        #
        self.row1.addWidget(self.rate_text)
        self.row1.addWidget(self.rate_input)
        self.row1.addWidget(self.initial_text)
        self.row1.addWidget(self.initial_input)
        self.row1.addWidget(self.years_text)
        self.row1.addWidget(self.years_input)
        self.row1.addWidget(self.dark_mode)

        #
        self.col1.addWidget(self.tree_view)
        self.col1.addWidget(self.calc_button)
        self.col1.addWidget(self.clear_button)
        self.col1.addWidget(self.save_button)

        self.col2.addWidget(self.canvas)

        self.row2.addLayout(self.col1, 30)
        self.row2.addLayout(self.col2, 70)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)

        main_window.setLayout(self.master_layout)
        self.setCentralWidget(main_window)

        self.calc_button.clicked.connect(self.calc_interest)
        self.clear_button.clicked.connect(self.reset)
        self.save_button.clicked.connect(self.save_data)
        self.dark_mode.stateChanged.connect(self.toggle_mode)

        self.apply_styles()

    def calc_interest(self):
        initial_investment = None
        try:
            interest_rate = float(self.rate_input.text())
            initial_investment = float(self.initial_input.text())
            num_years = int(self.years_input.text())

        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input, enter a number!")
            return

        total = initial_investment

        for year in range(1, num_years + 1):
            total += total * (interest_rate / 100)
            item_year = QStandardItem(str(year))
            item_total = QStandardItem("{:.2f}".format(total))
            self.model.appendRow([item_year, item_total])

        # Update chart with data
        self.figure.clear()
        ax = self.figure.subplots()
        years = list(range(1, num_years + 1))
        totals = [initial_investment * (1 + interest_rate/100)**year
                  for year in years]

        ax.plot(years, totals)
        ax.set_title("Interest Chart")
        ax.set_xlabel("Year")
        ax.set_ylabel("Total")
        self.canvas.draw()

    def save_data(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if dir_path:
            folder_path = os.path.join(dir_path, "Saved")
            os.makedirs(folder_path, exist_ok=True)

            file_path = os.path.join(folder_path, "results.csv")
            with open(file_path, "w") as file:
                file.write("Year, Total\n")
                for row in range(self.model.rowCount()):
                    year = self.model.index(row, 0).data()
                    total = self.model.index(row, 1).data()
                    file.write(f'{year}, {total}\n')

            plt.savefig("Saved/chart.png")

            QMessageBox.information(self, "Save Reusults",
                                "Results were saved to your Folder")

        else:
            QMessageBox.warning(self, "Save Results", "No directory selected")

    def reset(self):
        self.rate_input.clear()
        self.initial_input.clear()
        self.years_input.clear()
        self.model.clear()

        self.figure.clear()
        self.canvas.draw()

    def apply_styles(self):

        self.setStyleSheet(
            """
            FinanceApp {
                background-color: #f0f0f0;
            }

            QLabel, QLineEdit, QPushButton {
                background-color: #f8f8f8;
            }

            QTreeView {
                background-color: #ffffff;
            }

            """
        )

        if self.dark_mode.isChecked():
            self.setStyleSheet(
                """
                FinanceApp {
                    background-color: #222222;
                }

                QLabel, QLineEdit, QPushButton {
                    background-color: #333333;
                    color: #eeeeee;
                }

                QTreeView {
                    background-color: #444444;
                    color: #eeeeee;
                }

                """
            )

    def toggle_mode(self):
        self.apply_styles()


if __name__ == "__main__":
    app = QApplication([])
    my_app = FinanceApp()
    my_app.show()
    app.exec_()
