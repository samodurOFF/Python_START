"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

my_list = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]


def del_el(x_list, el):
    while True:
        try:
            x_list.remove(el)
        except ValueError:
            return x_list


i = 0
while i < len(my_list):
    if my_list.count(my_list[i]) > 1:
        my_list = del_el(my_list, my_list[i])
    else:
        i += 1
print(my_list)
