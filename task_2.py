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

from random import randint
import math


def get_num(n, frst, last):
    return [randint(frst, last) for i in range(n)]


def mult_pairs(mylist):
    return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist) / 2))]


n = int(input('Введите число элементов списка N: '))
frst = int(input('Введите минимальное число списка Min: '))
last = int(input('Введите максимальное число списка Max: '))

mylist = get_num(n, frst, last)
print(mylist)
print(mult_pairs(mylist))