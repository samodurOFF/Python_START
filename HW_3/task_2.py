"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]

[2, 3, 5, 6]
[12, 15]
"""
import random
import math
new_list = [random.randint(1, 9)
            for r in range(int(input('Введите размер списка: ')))]
print(new_list)
multi_list = []
size = math.ceil(len(new_list)/2)
for el in range(size):
    multi_list.append(new_list[el] * new_list[-el - 1])
print(multi_list)
