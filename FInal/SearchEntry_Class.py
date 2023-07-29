# Joebeck Andrew F. Gusi | BSCPE 1-5 | Final Project |

import csv

class SearchEntry:
    def __init__(self):
        # Initialize any required variables
        pass

    def search_by_name(self, name):
        # Implement code to search for entries by name
        with open('respondent_data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            found_entries = [row for row in reader if name.lower() in row[0].lower()]
        return found_entries

    # Implement other search methods as needed
