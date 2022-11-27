"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""
from math import factorial

number = int(input("Введите натуральное число: "))

# Вариант 1
result = []
for num in range(1, number + 1):
    result.append(factorial(num))
print(result)

# Вариант 2
result = [factorial(num) for num in range(1, number + 1)]
print(result)
