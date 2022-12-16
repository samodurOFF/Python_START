"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""
from random import  randrange
n = int(input('Введите количество элементов: '))
a = [randrange (0, 10) for i in range (n)]
print(a)
new_list = []
new_list.append(a[0])
for idx in range(len(a) - 1):
     if a[idx] != a[idx + 1]:
        new_list.append(a[idx + 1])
print(new_list)