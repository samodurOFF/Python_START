from logger import log
import json


@log
def get_data() -> list:

    with open("HW_7\db.json", 'r', encoding="utf-8") as file:
        data_file = json.load(file)
    return data_file["items"]


@log
def get_data_id(id: int) -> dict:

    with open("db.json", "r", encoding="utf-8") as file:
        data_file = json.load(file)
        for item in data_file['items']:
            if item['id'] == id:
                return item


@log
def get_data_last_name(last_name: str) -> list:

    res = []
    with open("db.json", "r", encoding="utf-8") as file:
        data_file = json.load(file)
        for item in data_file['items']:
            if item['last_name'].lower() == last_name.lower():
                res.append(item)
    return res


@log
def add_data(data: dict):
    id = data.get("id")

    with open("HW_7\db.json", 'r', encoding="utf-8") as file:
        data_file = json.load(file)

    if id:
        for i, items in enumerate(data_file["items"]):
            if id == items["id"]:
                data_file["items"][i] = data
                break

    else:
        id = data_file["last_id"]["id"] + 1
        data_file["last_id"]["id"] = id
        data["id"] = id
        data_file["items"].append(data)

    with open("HW_7\db.json", "w", encoding="utf-8") as file:
        json.dump(data_file, file, indent=2, ensure_ascii=False)