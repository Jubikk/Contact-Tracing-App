
import tkinter as tk
import csv
from tkinter import messagebox
from Testtt import ContactTracer
from Testing import Contact


class ContactTracerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('COVID Contact Tracing App')

        self.tracer = ContactTracer()

        self.name_label = tk.Label(root, text='Name:')
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()  

        self.phone_label = tk.Label(root, text='Phone:')
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text='Email:')
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.add_button = tk.Button(root, text='Add Contact', command=self.add_contact)
        self.add_button.pack()

        self.search_button = tk.Button(root, text='Search Contact', command=self.search_contact)
        self.search_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        contact = Contact(name, phone, email)
        self.tracer.add_contact(contact)

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

        messagebox.showinfo('Success', 'Contact added successfully.')

        self.write_to_csv()

    def search_contact(self):
        name = self.name_entry.get()
        contact = self.tracer.search_contact(name)

        if contact:
            messagebox.showinfo('Contact Details', f'Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}')
        else:
            messagebox.showinfo('Contact Not Found', 'No contact found with the provided name.')

    def write_to_csv(self):
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Email'])
            writer.writeheader()
            for contact in self.tracer.contacts:
                writer.writerow(contact.to_dict())

if __name__ == '_main_':
    root = tk.Tk()
    app = ContactTracerGUI(root)
    root.mainloop()