"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

number = int(input("Введите натуральное число: "))

my_list = [0 for _ in range(number * 2 + 1)]
my_list[number + 1] = my_list[number - 1] = 1
for i in range(number - 1):
    my_list[number + 2 + i] = my_list[number + 1 + i] + my_list[number + i]
    my_list[number - 2 - i] = my_list[number + 2 + i] * ((-1) ** (i + 1))
print(my_list)