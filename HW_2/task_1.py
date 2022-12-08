"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0 -> 23
0.56 -> 11          """

from decimal import Decimal

number = input('Введите вещественное число ')
sum = 0
for i in number:
    if i.isdigit():
        sum = sum + int(i)
print(f"Сумма цифр в числе {number} равна {sum}")

# Вариант с генератором
# num = input('Введите вещественное число ')
# sum = sum([int(i) for i in num if i.isdigit()])
# print(f"Сумма цифр в числе {num} равна {sum}")

# 3 вариант
# num = Decimal(input('N: '))

# while int(num) != num:
#     num *= 10
#     print(num)

# print(num)
# result = 0
# while num:
#     result += num % 10
#     num //= 10
# print(result)
