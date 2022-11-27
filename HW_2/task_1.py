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

import math

number = float(input("Введите вещественное число: "))

# Вариант 1
summa = sum([int(num) for num in str(number) if num.isdigit()])
print(f"Сумма чисел (вариант 1): {summa}")

# Варианты 2 и 3 работают очень не стабильно из-за неточностей при операциях с плавающей запятой

# # Вариант 2
# number_2 = number
# while number_2 != int(number_2):
#     number_2 *= 10
# summa = 0
# while number_2 > 0:
#     summa += number_2 % 10
#     number_2 //= 10
# print(f"Сумма чисел (вариант 2): {int(summa)}")
#
# # Вариант 3
# number_3 = number
# while number_3 != math.trunc(number_3):
#     number_3 *= 10
# number_3 = int(number_3)
# count = int(math.log10(number_3)) + 1
# summa = 0
# for _ in range(count):
#     summa += number_3 % 10
#     number_3 //= 10
# print(f"Сумма чисел (вариант 3): {summa}")

