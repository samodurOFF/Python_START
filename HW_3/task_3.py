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

def get_real_nums (n, first, extreme):
    return [round(uniform(first, extreme), 2) for i in range(n)]

def find_diff(my_num):
    num = [round(x - int(x), 2) for x in (my_num)]
    return max(num) - min(num)

n = 5
first = 1
extreme = 10
my_num = get_real_nums(n, first, extreme)

print (my_num)
print(find_diff(my_num))
