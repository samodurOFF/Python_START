"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""

n = input('Введите вещественное число ')
str_n = str(n)
str_n = str_n.replace('.', '')

my_list = list(str_n)
my_list = map(int, my_list)
print(sum(my_list))
