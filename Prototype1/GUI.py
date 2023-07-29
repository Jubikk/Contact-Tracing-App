# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import cv2
from ContactTracingClass import ContactTracer
from ContactClass import Contact


class ContactTracerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('COVID Contact Tracing App')
        self.tracer = ContactTracer()

        self.style = ttk.Style()
        self.style.configure('Title.TLabel', font=('Helvetica', 18, 'bold'))
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))

        self.title_label = ttk.Label(root, text='COVID Contact Tracing', style='Title.TLabel')
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = ttk.Label(root, text='Name:')
        self.name_label.grid(row=1, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.age_label = ttk.Label(root, text='Age:')
        self.age_label.grid(row=2, column=0, sticky=tk.W)
        self.age_entry = ttk.Entry(root)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        self.gender_label = ttk.Label(root, text='Gender:')
        self.gender_label.grid(row=3, column=0, sticky=tk.W)
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(root, textvariable=self.gender_var, values=['Male', 'Female', 'Other'])
        self.gender_combobox.grid(row=3, column=1, padx=5, pady=5)

        self.phone_label = ttk.Label(root, text='Phone:')
        self.phone_label.grid(row=4, column=0, sticky=tk.W)
        self.phone_entry = ttk.Entry(root)
        self.phone_entry.grid(row=4, column=1)

        self.email_label = ttk.Label(root, text='Email:')
        self.email_label.grid(row=5, column=0, sticky=tk.W)
        self.email_entry = ttk.Entry(root)
        self.email_entry.grid(row=5, column=1)

        self.address_label = ttk.Label(root, text='Address:')
        self.address_label.grid(row=6, column=0, sticky=tk.W)
        self.address_entry = ttk.Entry(root)
        self.address_entry.grid(row=6, column=1)

        self.num_vaccines_label = ttk.Label(root, text='Number of Vaccines:')
        self.num_vaccines_label.grid(row=7, column=0, sticky=tk.W)
        self.num_vaccines_entry = ttk.Entry(root)
        self.num_vaccines_entry.grid(row=7, column=1)

        self.symptoms_label = ttk.Label(root, text='Symptoms:')
        self.symptoms_label.grid(row=8, column=0, sticky=tk.W)
        self.symptoms_entry = ttk.Entry(root)
        self.symptoms_entry.grid(row=8, column=1)

        self.travel_history_label = ttk.Label(root, text='Travel History:')
        self.travel_history_label.grid(row=9, column=0, sticky=tk.W)
        self.travel_history_entry = ttk.Entry(root)
        self.travel_history_entry.grid(row=9, column=1)

        self.covid_encounter_label = ttk.Label(root, text='Encounter with COVID:')
        self.covid_encounter_label.grid(row=10, column=0, sticky=tk.W)
        self.covid_encounter_entry = ttk.Entry(root)
        self.covid_encounter_entry.grid(row=10, column=1)

        self.add_button = ttk.Button(root, text='Add Contact', command=self.add_contact)
        self.add_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        self.search_button = ttk.Button(root, text='Search Contact', command=self.search_contact)
        self.search_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        self.tree = ttk.Treeview(root, columns=['Name', 'Age', 'Gender', 'Phone', 'Email', 'Address', 'Vaccines', 'Symptoms', 'Travel History', 'COVID Encounter'], show='headings', style='Treeview')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Age', text='Age')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Address', text='Address')
        self.tree.heading('Vaccines', text='Vaccines')
        self.tree.heading('Symptoms', text='Symptoms')
        self.tree.heading('Travel History', text='Travel History')
        self.tree.heading('COVID Encounter', text='COVID Encounter')
        self.tree.grid(row=13, column=0, columnspan=2, padx=10, pady=10)
        self.capture_button = ttk.Button(root, text='Capture Image', command=self.capture_image)
        self.capture_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

    def capture_image(self):
            # Capture image using OpenCV
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            camera.release()

            # Save the captured image in the 'captures' folder
            image_path = 'captures/captured_image.png'
            cv2.imwrite(image_path, image)

            # Save the image path in a text file
            with open('captures/image_path.txt', 'w') as file:
                file.write(image_path)

            messagebox.showinfo('Success', 'Image captured successfully.')
    def add_contact(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        num_vaccines = self.num_vaccines_entry.get()
        symptoms = self.symptoms_entry.get()
        travel_history = self.travel_history_entry.get()
        covid_encounter = self.covid_encounter_entry.get()

        # Check if required fields are not empty
        if not name.strip() or not age.strip():
            messagebox.showerror('Error', 'Name and age fields are required.')
            return

        # Check if age is numeric
        if not age.isnumeric():
            messagebox.showerror('Error', 'Age must be a numeric value.')
            return

        # Check if number of vaccines is numeric
        if num_vaccines and not num_vaccines.isnumeric():
            messagebox.showerror('Error', 'Number of vaccines must be a numeric value.')
            return

        contact = Contact(name, age, gender, phone, email, address, num_vaccines, symptoms, travel_history, covid_encounter)
        self.tracer.add_contact(contact)

        self.clear_entries()

        messagebox.showinfo('Success', 'Contact added successfully.')

        self.write_to_csv()

    def search_contact(self):
        name = self.name_entry.get()
        contact = self.tracer.search_contact(name)

        if contact:
            result_window = tk.Toplevel(self.root)
            result_window.title('Contact Details')
            result_label = ttk.Label(result_window, text=f'Name: {contact.name}\nAge: {contact.age}\nGender: {contact.gender}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\nVaccines: {contact.num_vaccines}\nSymptoms: {contact.symptoms}\nTravel History: {contact.travel_history}\nCOVID Encounter: {contact.covid_encounter}')
            result_label.pack()
        else:
            messagebox.showinfo('Contact Not Found', 'No contact found with the provided name.')

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_combobox.set('')
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.num_vaccines_entry.delete(0, tk.END)
        self.symptoms_entry.delete(0, tk.END)
        self.travel_history_entry.delete(0, tk.END)
        self.covid_encounter_entry.delete(0, tk.END)

    def write_to_csv(self):
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Gender', 'Phone', 'Email', 'Address', 'Vaccines', 'Symptoms', 'Travel History', 'COVID Encounter'])
            writer.writeheader()
            for contact in self.tracer.contacts:
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

if __name__ == '__main__':
    root = ThemedTk(theme="blue")
    app = ContactTracerGUI(root)
    root.mainloop()