"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""

from random import randint

def get_list(n, first, extreme):
    return [randint(first, extreme) for i in range(n)]

def sum_odd_position(my_list):
    return sum(my_list[1::2])

n = 10
first = 1
extreme = 10

my_list = get_list(n, first, extreme)
print(my_list)
print(sum_odd_position(my_list))
