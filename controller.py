# Модуль controller
from model import PhoneBook
from view import PhoneBookView

class PhoneBookController:
    def __init__(self, file_path):
        self.phone_book = PhoneBook(file_path)

    def show_contacts(self):
        contacts = self.phone_book.contacts
        PhoneBookView.print_contacts(contacts)

    def add_contact(self):
        name, phone_number = PhoneBookView.get_contact_details()
        self.phone_book.add_contact(name, phone_number)
        self.phone_book.save_contacts()

    def search_contact(self):
        keyword = PhoneBookView.get_search_keyword()
        self.phone_book.search_contact(keyword)

    def update_contact(self):
        name, phone_number = PhoneBookView.get_update_details()
        self.phone_book.update_contact(name, phone_number)
        self.phone_book.save_contacts()

    def delete_contact(self):
        name = PhoneBookView.get_delete_name()
        self.phone_book.delete_contact(name)
        self.phone_book.save_contacts()

    def export_contacts(self):
        self.phone_book.save_contacts()
        PhoneBookView.print_export_success()

    def import_contacts(self):
        self.phone_book.load_contacts()
        PhoneBookView.print_import_success()
