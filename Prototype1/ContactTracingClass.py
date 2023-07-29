# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

import csv
from tkinter import messagebox
from ContactClass import Contact

class ContactTracer:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def write_to_csv(self):
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Gender', 'Phone', 'Email', 'Address', 'Vaccines', 'Symptoms', 'Travel History', 'COVID Encounter'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({
                    'Name': contact.name,
                    'Age': contact.age,
                    'Gender': contact.gender,
                    'Phone': contact.phone,
                    'Email': contact.email,
                    'Address': contact.address,
                    'Vaccines': contact.num_vaccines,
                    'Symptoms': contact.symptoms,
                    'Travel History': contact.travel_history,
                    'COVID Encounter': contact.covid_encounter
                })
