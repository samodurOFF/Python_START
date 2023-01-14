from asyncio import constants


path = 'phonebook.txt'
contacts = []

def read_file():
    global contacts
    with open(path) as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    return contacts

def get_contacts():
    global contacts
    return contacts

def add_contact():
    global contacts
    id = input('Введите id: ')
    name = input('Введите name: ')
    phone = input('Введите phone: ')
    comment = input('Введите comment: ')
    contacts.append(';'.join([id, name, phone, comment]))

def save_file():
    global contacts
    with open(path, 'w', encoding='utf-8') as f:
        pass