# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QDialog, QHeaderView, QMessageBox, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QSize, QThread
import csv

class AdminWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Set dialog properties
        self.setWindowTitle('Admin Window')
        self.setWindowModality(Qt.ApplicationModal)
        self.setMinimumSize(QSize(800, 600))

        # Create search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search...')
        self.search_bar.textChanged.connect(self.search)

        # Create search button
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search)

        # Create reset button
        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset)

        # Create table widget
        self.table = QTableWidget()
        self.table.setColumnCount(13)
        self.table.setHorizontalHeaderLabels(['Name', 'Age', 'Gender', 'Phone', 'Email', 'Address', 'Vaccine', 'Symptoms', 'Contact history', 'Testing', 'Travel history', 'Photo', 'Timestamp'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Load data from CSV file
        self.load_data()

        # Create layout
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)
        search_layout.addWidget(self.reset_button)

        layout = QVBoxLayout()
        layout.addLayout(search_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_data(self):
        # Clear table
        self.table.setRowCount(0)

        # Load data from CSV file
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                age = row[1]
                gender = row[2]
                phone = row[3]
                email = row[4]
                address = row[5]
                vaccine = row[6]
                symptoms = row[7]
                contact_history = row[8]
                testing = row[9]
                travel_history = row[10]
                photo = row[11]
                timestamp = row[12]

                # Add row to table
                self.table.insertRow(self.table.rowCount())
                self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(name))
                self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(age))
                self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(gender))
                self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(phone))
                self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem(email))
                self.table.setItem(self.table.rowCount() - 1, 5, QTableWidgetItem(address))
                self.table.setItem(self.table.rowCount() - 1, 6, QTableWidgetItem(vaccine))
                self.table.setItem(self.table.rowCount() - 1, 7, QTableWidgetItem(symptoms))
                self.table.setItem(self.table.rowCount() - 1, 8, QTableWidgetItem(contact_history))
                self.table.setItem(self.table.rowCount() - 1, 9, QTableWidgetItem(testing))
                self.table.setItem(self.table.rowCount() - 1, 10, QTableWidgetItem(travel_history))
                self.table.setItem(self.table.rowCount() - 1, 11, QTableWidgetItem(photo))
                self.table.setItem(self.table.rowCount() - 1, 12, QTableWidgetItem(timestamp))

    def save_data(self):
        # Save data to CSV file
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in range(self.table.rowCount()):
                name = self.table.item(row, 0).text()
                age = self.table.item(row, 1).text()
                gender = self.table.item(row, 2).text()
                phone = self.table.item(row, 3).text()
                email = self.table.item(row, 4).text()
                address = self.table.item(row, 5).text()
                vaccine = self.table.item(row, 6).text()
                symptoms = self.table.item(row, 7).text()
                contact_history = self.table.item(row, 8).text()
                testing = self.table.item(row, 9).text()
                travel_history = self.table.item(row, 10).text()
                photo = self.table.item(row, 11).text()
                timestamp = self.table.item(row, 12).text()

                writer.writerow([name, age, gender, phone,email, address, vaccine, symptoms, contact_history, testing, travel_history, photo, timestamp])

    def search(self):
        search_text = self.search_bar.text().lower()

        # Clear table
        self.table.setRowCount(0)

        # Load data from CSV file and add matching rows to table
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if search_text in ','.join(row).lower():
                    name = row[0]
                    age = row[1]
                    gender = row[2]
                    phone = row[3]
                    email = row[4]
                    address = row[5]
                    vaccine = row[6]
                    symptoms = row[7]
                    contact_history = row[8]
                    testing = row[9]
                    travel_history = row[10]
                    photo = row[11]
                    timestamp = row[12]

                    self.table.insertRow(self.table.rowCount())
                    self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(name))
                    self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(age))
                    self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(gender))
                    self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(phone))
                    self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem(email))
                    self.table.setItem(self.table.rowCount() - 1, 5, QTableWidgetItem(address))
                    self.table.setItem(self.table.rowCount() - 1, 6, QTableWidgetItem(vaccine))
                    self.table.setItem(self.table.rowCount() - 1, 7, QTableWidgetItem(symptoms))
                    self.table.setItem(self.table.rowCount() - 1, 8, QTableWidgetItem(contact_history))
                    self.table.setItem(self.table.rowCount() - 1, 9, QTableWidgetItem(testing))
                    self.table.setItem(self.table.rowCount() - 1, 10, QTableWidgetItem(travel_history))
                    self.table.setItem(self.table.rowCount() - 1, 11, QTableWidgetItem(photo))
                    self.table.setItem(self.table.rowCount() - 1, 12, QTableWidgetItem(timestamp))

    def reset(self):
        # Clear search bar
        self.search_bar.clear()

        # Reload data
        self.load_data()

    def closeEvent(self, event):
        # Save data before closing
        self.save_data()

        # Confirm closing the window
        reply = QMessageBox.question(self, 'Confirm Closing', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()