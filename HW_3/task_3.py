"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
from random import uniform
from math import modf

number = int(input("Введите натуральное число: "))
my_list = [round(uniform(1, 10), 2) for _ in range(number)]
print(my_list)
frac_list = [modf(el)[0] for el in my_list]
print(round(max(frac_list) - min(frac_list), 2) * 100)
