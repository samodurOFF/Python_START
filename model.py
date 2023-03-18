# Модуль model

import os

class PhoneBook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = {}
        if os.path.exists(file_path):
            self.load_contacts()

    def load_contacts(self):
        with open(self.file_path, 'r') as f:
            for line in f:
                data = line.strip().split(';')
                self.contacts[data[0]] = data[1:]

    def save_contacts(self):
        with open(self.file_path, 'w') as f:
            for name, details in self.contacts.items():
                f.write(f'{name};{";".join(details)}\n')

    def add_contact(self, name, phone_number):
        self.contacts[name] = [phone_number]

    def search_contact(self, keyword):
        for name, details in self.contacts.items():
            if keyword in name or keyword in details:
                print(f'{name}: {", ".join(details)}')

    def update_contact(self, name, phone_number):
        if name in self.contacts:
            self.contacts[name] = [phone_number]

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
