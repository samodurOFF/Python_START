from logger import log
import json
from os import path


def get_data() -> list:
    """
    Выгружает данные из файла и возвращает список словарей

    """
    if path.isfile("db.json"):
        with open("db.json", 'r', encoding="utf-8") as file:
            data_file = json.load(file)
        return data_file
    else:
        return []


def add_data(data: dict):
    """
    Принимает словарь с записью и добавляет в файл..
    :param data:
    :return:
    """
    if path.isfile("db.json"):
        with open("db.json", 'r', encoding ='utf-8') as file:
            data_file = json.load(file)
    else:
        data_file = []

    if not data['id']:
        id = len(data_file) + 1
        data['id'] = id

    data_file.append(data)

    with open("db.json", "w", encoding="utf-8") as file:
        json.dump(data_file, file, indent=2, ensure_ascii=False)

