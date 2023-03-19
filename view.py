class PhoneBookView:
    @staticmethod
    def print_menu():
        print("1. Показать контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Обновить контакт")
        print("5. Удалить контакт")
        print("6. Экспорт контактов")
        print("7. Импорт контактов")
        print("0. Выход")

    @staticmethod
    def get_contact_details():
        name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        return name, phone_number

    @staticmethod
    def get_search_keyword():
        keyword = input("Введите ключевое слово для поиска: ")
        return keyword

    @staticmethod
    def get_update_details():
        name = input("Введите имя контакта, который хотите обновить: ")
        phone_number = input("Введите новый номер телефона: ")
        return name, phone_number

    @staticmethod
    def get_delete_name():
        name = input("Введите имя контакта, который хотите удалить: ")
        return name

    @staticmethod
    def print_contacts(contacts):
        if not contacts:
            print("Нет контактов")
        else:
            for name, details in contacts.items():
                print(f'{name}: {", ".join(details)}')

    @staticmethod
    def print_export_success():
        print("Контакты успешно экспортированы в файл")

    @staticmethod
    def print_import_success():
        print("Контакты успешно импортированы из файла")
