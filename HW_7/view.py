from logger import log


@log
def grettings():
    '''Приветствие'''
    print('Я справочник')


@log
def menu() -> str:
    '''Меню справочника'''
    return input('Выберите пункт меню: \n'
                 '1 - показать справочник \n'
                 '2 - добавить запись \n'
                 '3 - выход \n')


@log
def print_book(data: list):
    for el in data:
        print(
            f'Имя: {el["first_name"]} | {el["last_name"]} | {el["phone_number"]} | {el["birthda"]} | {el["workplace"]} | {el["id"]}')
    if not data:
        print('Нет данных для отображения')


@log
def input_data():
    book = {}
    book['id'] = ''
    book["first_name"] = input('Введите имя: ')
    book["last_name"] = input('Введите фамилию: ')
    book["phone_number"] = input('Введите телефон: ')
    book["birthda"] = input('Введите дату рождения: ')
    book["workplace"] = input('Введите место работы: ')
    return book

