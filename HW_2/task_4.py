"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""

from random import randint

number = int(input("Введите натуральное число: "))
my_list = []
for _ in range(number):
    my_list.append(randint(-number, number))
res = 1
with open('indexes.txt', 'r') as file:
    for line in file:
        index = int(line)
        if len(my_list) > index >= -len(my_list):
            res *= my_list[index]

print("ответ", res)
