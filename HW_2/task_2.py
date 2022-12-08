"""
Напишите программу, которая принимает на вход натуральное число N и 
выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""

n = ''
while not n.isdigit():
    n = input('Введите натуральное число N: ')

n = int(n)
result = []
f = 1
for i in range(1, n + 1):
    f = f * i
    result.append(f)
print(result)


# Вариант Ивана (с генератором списка)

# from math import factorial

# number = int(input('Введите натуральное число N: '))

# print([factorial(num) for num in range(1, number + 1)])
