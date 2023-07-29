# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

import csv

class AddEntry:
    def __init__(self):
        # Initialize any required variables
        pass

    def add_respondent_and_contact_details(self, first_name, middle_name, last_name, age, gender, phone, email, address, vaccine_status, vaccine_type, symptoms, traveled, covid_contact, contact_name, contact_age, contact_phone, contact_email, contact_relationship):
        # Implement code to add respondent and contact details to the CSV data file
        with open('respondent_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, middle_name, last_name, age, gender, phone, email, address, vaccine_status, vaccine_type, symptoms, traveled, covid_contact, contact_name, contact_age, contact_phone, contact_email, contact_relationship])
