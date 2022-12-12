"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""


"""
str_text = "автобус, генерал швабра итог арбуз вагон"
str_num = []

value = str_text.split()
for i in value :
    if not ("a" in i and "б" in i and "в" in i):
        str_num.append(i)

result = " ".join(str_num) 
print(result)      
"""

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

