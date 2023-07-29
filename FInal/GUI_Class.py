# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

import re
import tkinter as tk
from tkinter import RIGHT, ttk
from AddEntry_Class import AddEntry
from SearchEntry_Class import SearchEntry
from tkinter import messagebox
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk


class CovidTracingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.title("COVID-19 Tracing App")
        self.geometry("800x700")

        # Initialize the list to store symptom variables
        self.symptoms_vars = []
        self.symptoms_var = tk.StringVar()

        # Set ttk theme using ThemedStyle
        self.style = ThemedStyle(self)
        self.style.set_theme("blue")

        self.style.configure("TButton", background="#820000", foreground="#820000", font=("Gothic", 10))
        self.style.configure("Emphasized.TButton", background="#820000", font=("Gothic", 10, "bold"))

        self.background_image = Image.open("PUP.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.label = tk.Label(self, image=self.background_photo)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        # Define the symptoms options
        self.checkboxes_symptoms = [
            ("Fever", "Fever"),
            ("Cough", "Cough"),
            ("Shortness of breath", "Shortness of breath or difficulty breathing"),
            ("Body aches", "Body aches"),
            ("Headache", "Headache"),
            ("New loss of taste or smell", "New loss of taste or smell"),
            ("Sore throat", "Sore throat"),
            ("Vomiting", "Vomiting"),
            ("Runny nose", "Runny nose"),
            ("None", "None")
        ]

        # Initialize the contact details variables
        self.contact_name_var = tk.StringVar()
        self.contact_age_var = tk.StringVar()
        self.contact_phone_var = tk.StringVar()
        self.contact_email_var = tk.StringVar()
        self.contact_relationship_var = tk.StringVar()

        # Create and layout the GUI widgets
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_first_name = ttk.Entry(self)
        self.entry_first_name.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Middle Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_middle_name = ttk.Entry(self)    
        self.entry_middle_name.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_last_name = ttk.Entry(self)
        self.entry_last_name.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self, text="Age:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_age = ttk.Entry(self)
        self.entry_age.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self, text="Gender:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.gender_var = tk.StringVar()
        self.gender_options = ["Male", "Female", "Transgender", "Gender Neutral", "Non-Binary", "Agender",
                               "Pangender", "Genderqueer", "Prefer Not to Say"]
        self.combobox_gender = ttk.Combobox(self, textvariable=self.gender_var, values=self.gender_options)
        self.combobox_gender.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self, text="Phone:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_phone = ttk.Entry(self)
        self.entry_phone.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(self, text="Email:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entry_email = ttk.Entry(self)
        self.entry_email.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(self, text="Address:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.entry_address = ttk.Entry(self)
        self.entry_address.grid(row=7, column=1, padx=10, pady=5)

        ttk.Label(self, text="Vaccine:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.vaccine_var = tk.StringVar()
        self.vaccine_options = ["1st shot", "2nd shot", "1st booster", "2nd booster", "None"]
        self.combobox_vaccine = ttk.Combobox(self, textvariable=self.vaccine_var, values=self.vaccine_options)
        self.combobox_vaccine.grid(row=8, column=1, padx=10, pady=5)

        ttk.Label(self, text="Vaccine Type:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.vaccine_type_var = tk.StringVar()
        self.vaccine_type_options = ["Pfizer", "Moderna", "Sputnik", "Covovax", "Janssen", "None"]
        self.combobox_vaccine_type = ttk.Combobox(self, textvariable=self.vaccine_type_var, values=self.vaccine_type_options)
        self.combobox_vaccine_type.grid(row=9, column=1, padx=10, pady=5)

        ttk.Label(self, text="Symptoms:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.symptoms_var = tk.StringVar()
        ttk.Label(self, textvariable=self.symptoms_var, relief="solid", width=40).grid(row=10, column=1, padx=10, pady=5, sticky="w")
        ttk.Button(self, text="Select Symptoms", command=self.open_symptoms_window).grid(row=10, column=2, padx=10, pady=5, sticky="w")

        ttk.Label(self, text="Traveled in past 14 days:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.travel_var = tk.StringVar(value="No")
        ttk.OptionMenu(self, self.travel_var, "No", "Yes", "No").grid(row=11, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self, text="Encountered someone with COVID-19:").grid(row=12, column=0, padx=10, pady=5, sticky="w")
        self.covid_contact_var = tk.StringVar(value="No")
        ttk.OptionMenu(self, self.covid_contact_var, "No", "Yes", "No").grid(row=12, column=1, padx=10, pady=5, sticky="w")

        # Contact Person Details
        ttk.Label(self, text="Contact Person Details", font=("Helvetica", 14, "bold")).grid(row=15, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        ttk.Label(self, text="Name:").grid(row=16, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact_name = ttk.Entry(self)
        self.entry_contact_name.grid(row=16, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="Age:").grid(row=17, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact_age = ttk.Entry(self)
        self.entry_contact_age.grid(row=17, column=1, padx=10, pady=5)

        ttk.Label(self, text="Phone:").grid(row=18, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact_phone = ttk.Entry(self)
        self.entry_contact_phone.grid(row=18, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="Email:").grid(row=19, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact_email = ttk.Entry(self)
        self.entry_contact_email.grid(row=19, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="Relationship:").grid(row=20, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact_relationship = ttk.Entry(self)
        self.entry_contact_relationship.grid(row=20, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        ttk.Button(self, text="Submit", command=self.add_respondent_and_contact_details).grid(row=23, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        ttk.Button(self, text="Search", command=self.search_respondent_details).grid(row=23, column=2, columnspan=2, padx=10, pady=10, sticky="ew")
    

    def open_symptoms_window(self):
        symptoms_window = tk.Toplevel(self)
        symptoms_window.title("Select Symptoms")
        ttk.Label(symptoms_window, text="Select Symptoms:").pack()

        # Create symptoms variables
        self.symptoms_vars = [tk.BooleanVar(value=False) for _ in self.checkboxes_symptoms]
        for i, (text, value) in enumerate(self.checkboxes_symptoms):
            ttk.Checkbutton(symptoms_window, text=text, variable=self.symptoms_vars[i]).pack()

        selected_symptoms_var = tk.StringVar()
        ttk.Button(symptoms_window, text="OK", command=lambda: self.update_selected_symptoms(symptoms_window, selected_symptoms_var)).pack()

    def get_symptom_var(self, var):
        # Find the corresponding symptom text based on the given BooleanVar
        for symptom_text, symptom_var in self.checkboxes_symptoms:
            if symptom_var is var:
                return symptom_text
        return None

    def update_selected_symptoms(self, symptoms_window, selected_symptoms_var):
        selected_symptoms = []
        for i, var in enumerate(self.symptoms_vars):
            if var.get():
                selected_symptoms.append(self.get_symptom_var(var))
        selected_symptoms_var.set(", ".join(selected_symptoms) if selected_symptoms else "")
        self.symptoms_var.set(selected_symptoms_var.get())
        symptoms_window.destroy()
    
    def update_selected_symptoms(self, symptoms_window, selected_symptoms_var):
        selected_symptoms = [text for var, (text, _) in zip(self.symptoms_vars, self.checkboxes_symptoms) if var.get()]
        selected_symptoms_var.set(", ".join(selected_symptoms) if selected_symptoms else "")
        self.symptoms_var.set(selected_symptoms_var.get())
        symptoms_window.destroy()

        # Implement code to collect data from GUI and add respondent details to CSV file
        first_name = self.entry_first_name.get()
        middle_name = self.entry_middle_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        vaccine_status = self.vaccine_var.get()
        vaccine_type = self.vaccine_type_var.get()
        symptoms = ", ".join([self.symptoms_vars[i].get() for i in range(len(self.symptoms_vars)) if self.symptoms_vars[i].get()])  # Join selected symptoms with a comma
        traveled = "Yes" if self.travel_var.get() else "No"
        covid_contact = "Yes" if self.covid_contact_var.get() else "No"
        
    def add_respondent_and_contact_details(self):
        # Collect data from GUI and add respondent details to CSV file
        first_name = self.entry_first_name.get()
        middle_name = self.entry_middle_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        vaccine_status = self.vaccine_var.get()
        vaccine_type = self.vaccine_type_var.get()
        symptoms = self.symptoms_var.get()
        traveled = self.travel_var.get()
        covid_contact = self.covid_contact_var.get()

        age = self.entry_age.get()
        if not age.isdigit() or int(age) <= 0:
            messagebox.showerror("Invalid Input", "Please enter a valid age (a positive integer).")
            return
        
        phone = self.entry_phone.get()
        if not re.match(r"^\d{11}$", phone):
            messagebox.showerror("Invalid Input", "Please enter a valid 11-digit phone number.")
            return
        
        selected_symptoms = ", ".join([text for var, (text, _) in zip(self.symptoms_vars, self.checkboxes_symptoms) if var.get()])
        symptoms = selected_symptoms if selected_symptoms else "None"
        traveled = "Yes" if self.travel_var.get() else "No"
        covid_contact = "Yes" if self.covid_contact_var.get() else "No"

        # Collect contact details
        contact_name = self.entry_contact_name.get()
        contact_age = self.entry_contact_age.get()
        contact_phone = self.entry_contact_phone.get()
        contact_email = self.entry_contact_email.get()
        contact_relationship = self.entry_contact_relationship.get()

        # Use the AddEntry class to add the respondent details to the CSV file
        add_entry = AddEntry()
        add_entry.add_respondent_and_contact_details(
            first_name, middle_name, last_name, age, gender, phone, email, address,
            vaccine_status, vaccine_type, symptoms, traveled, covid_contact,
            contact_name, contact_age, contact_phone, contact_email, contact_relationship
        )

        # Clear the entry fields after submission
        self.entry_first_name.delete(0, tk.END)
        self.entry_middle_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.gender_var.set("")
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.vaccine_var.set("")
        self.vaccine_type_var.set("")
        for var in self.symptoms_vars:
            var.set("")
        self.travel_var.set("No")
        self.covid_contact_var.set("No")
        self.entry_contact_name.delete(0, tk.END)
        self.entry_contact_age.delete(0, tk.END)
        self.entry_contact_phone.delete(0, tk.END)
        self.entry_contact_email.delete(0, tk.END)
        self.entry_contact_relationship.delete(0, tk.END)

        messagebox.showinfo("Submission Successful", "Data submitted successfully!")

    def search_respondent_details(self):
        # Implement code to open a new window showing search results
        search_window = tk.Toplevel(self)
        search_window.title("Search Respondent Details")

        ttk.Label(search_window, text="Search by Name:").grid(row=0, column=0, padx=10, pady=5)
        search_name_entry = ttk.Entry(search_window)
        search_name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Button(search_window, text="Search", command=lambda: self.display_search_results(search_name_entry.get())).grid(row=0, column=2, padx=10, pady=5)

    def display_search_results(self, name):
    # Implement code to display search results in a new window
        search_entry = SearchEntry()
        self.respondent_data = search_entry.search_by_name(name)
        print("Found Data:", self.respondent_data)  # Add this line to check the retrieved data

        if not self.respondent_data:
            messagebox.showinfo("No Results", "No results found for the given name.")
            return

        results_window = tk.Toplevel(self)
        results_window.title("Search Results")

        # Create a Treeview widget to display the data in tabular form with vertical and horizontal scrollbars
        columns = ("First Name", "Middle Name", "Last Name", "Age", "Gender", "Phone", "Email", "Address", "Vaccine", "Vaccine Type", "Symptoms", "Traveled", "Encountered COVID-19", "Contact Name", "Contact Age", "Contact Phone", "Contact Email", "Contact Relationship")
        tree = ttk.Treeview(results_window, columns=columns, show="headings")

        # Set the headings for each column
        for col in columns:
            tree.heading(col, text=col)

        # Create vertical and horizontal scrollbars
        v_scrollbar = ttk.Scrollbar(results_window, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(results_window, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack the Treeview and scrollbars, and configure column widths
        tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Add data to the Treeview
        for item in self.respondent_data:
        # Check if the item list has enough elements before accessing them
            if len(item) >= 18:
                rearranged_item = [
                    item[0],  # First Name
                    item[1],  # Middle Name
                    item[2],  # Last Name
                    item[3],  # Age
                    item[4],  # Gender
                    item[5],  # Phone
                    item[6],  # Email
                    item[7],  # Address
                    item[8],  # Vaccine
                    item[9],  # Vaccine Type
                    item[10],  # Symptoms (display horizontally as a string)
                    item[11],  # Traveled
                    item[12],  # Encountered COVID
                    item[13],  # Contact Name
                    item[14],  # Contact Age
                    item[15],  # Contact Phone
                    item[16],  # Contact Email
                    item[17],  # Contact Relationship
                ]
                tree.insert("", "end", values=rearranged_item)
            else:
                print(f"Row data is incomplete: {item}")

if __name__ == "__main__":
    app = CovidTracingApp()
    app.mainloop()
