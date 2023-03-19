from controller import PhoneBookController
from view import PhoneBookView

def main():
    file_path = 'phonebook.txt'
    phone_book_controller = PhoneBookController(file_path)
    PhoneBookView.print_menu()

    while True:
        choice = input("Введите номер действия: ")

        if choice == '1':
            phone_book_controller.show_contacts()
        elif choice == '2':
            phone_book_controller.add_contact()
        elif choice == '3':
            phone_book_controller.search_contact()
        elif choice == '4':
            phone_book_controller.update_contact()
        elif choice == '5':
            phone_book_controller.delete_contact()
        elif choice == '6':
            phone_book_controller.export_contacts()
        elif choice == '7':
            phone_book_controller.import_contacts()
        elif choice == '0':
            break
        else:
            print("Неверный номер действия")

if __name__ == '__main__':
    print("Добро пожаловать в телефонный справочник!")
    main()
