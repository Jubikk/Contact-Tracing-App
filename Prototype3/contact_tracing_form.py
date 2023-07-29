# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt


import cv2 
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QVBoxLayout


class ContactTracingForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Tracing Form")
        self.setFixedSize(400, 500)

        # Create widgets for the form
        self.name_label = QLabel("Name:")
        self.name_text = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_text = QLineEdit()

        self.gender_label = QLabel("Gender:")
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female", "Other"])

        self.phone_label = QLabel("Phone Number:")
        self.phone_text = QLineEdit()

        self.email_label = QLabel("Email Address:")
        self.email_text = QLineEdit()

        self.address_label = QLabel("Address:")
        self.address_text = QTextEdit()

        self.vaccine_status_label = QLabel("Vaccine Status:")
        self.vaccine_status_combo = QComboBox()
        self.vaccine_status_combo.addItems(["None", "1st Dose", "2nd Dose", "1st Booster", "2nd Booster"])

        self.symptoms_label = QLabel("Symptoms in the past 7 Days:")
        self.symptoms_text = QTextEdit()

        self.contact_history_label = QLabel("Have you had contact with someone with the Symptoms?")
        self.contact_history_combo = QComboBox()
        self.contact_history_combo.addItems(["Yes", "No"])

        self.covid_testing_label = QLabel("Have you been tested for Covid-19 for the past 10 days?")
        self.covid_testing_combo = QComboBox()
        self.covid_testing_combo.addItems(["Yes", "No"])

        self.travel_history_label = QLabel("Have you traveled internationally for the past 14 days?")
        self.travel_history_combo = QComboBox()
        self.travel_history_combo.addItems(["Yes", "No"])

        self.photo_label = QLabel("Photo:")
        self.photo_button = QPushButton("Take Photo")
        self.photo_button.clicked.connect(self.take_photo)

        self.photo_preview_label = QLabel()
        self.photo_preview_label.setFixedSize(200, 200)

        self.submit_button = QPushButton("Submit")

        # Add widgets to the form layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_text)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_text)
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_combo)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_text)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_text)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_text)
        layout.addWidget(self.vaccine_status_label)
        layout.addWidget(self.vaccine_status_combo)
        layout.addWidget(self.symptoms_label)
        layout.addWidget(self.symptoms_text)
        layout.addWidget(self.contact_history_label)
        layout.addWidget(self.contact_history_combo)
        layout.addWidget(self.covid_testing_label)
        layout.addWidget(self.covid_testing_combo)
        layout.addWidget(self.travel_history_label)
        layout.addWidget(self.travel_history_combo)
        layout.addWidget(self.photo_label)
        layout.addWidget(self.photo_button)
        layout.addWidget(self.photo_preview_label)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def take_photo(self):
        # Capture an image from the user's camera and display it on the form
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.photo_preview_label.setPixmap(QPixmap.fromImage(image))
        cap.release()