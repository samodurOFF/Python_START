"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""

text = "бамбуковый красный баобабовый синий барбарисовый фиолетовый"
# Хотел упростить первый вариант, получилось еще два, но проще не стало!
# Вариант_1
new_text = " ".join(list(filter(lambda x: not ("а" in x and "б" in x and "в" in x), text.split())))
print(new_text)

# Вариант_2
new_text = " ".join(list(filter(lambda x: not all(("а" in x, "б" in x, "в" in x)), text.split())))
print(new_text)

# Вариант_2
new_text = " ".join(list(filter(lambda x: not all(map(lambda y, z: z in y, ["абв"], x)), text.split())))
print(new_text)
