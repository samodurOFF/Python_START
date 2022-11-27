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
number_str = str(number)
summa = 0
for num in number_str:
    if num.isdigit():
        summa += int(num)
print(f"Сумма чисел (вариант 1): {summa}")

# Вариант 2
number_2 = number
while number_2 != int(number_2):
    number_2 *= 10
summa = 0
while number_2 > 0:
    summa += number_2 % 10
    number_2 //= 10
print(f"Сумма чисел (вариант 2): {int(summa)}")

# Вариант 3
while number != math.trunc(number):
    number *= 10
number = int(number)
count = int(math.log10(number)) + 1
summa = 0
for _ in range(count):
    summa += number % 10
    number //= 10
print(f"Сумма чисел (вариант 3): {summa}")
