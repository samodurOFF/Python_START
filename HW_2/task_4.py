"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt 
(в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""

from random import randint

num = int(input('Введите целое число N: '))
some_list = [randint(-num, num) for _ in range(num)]
print(some_list)
result = 1
with open('indexes.txt', 'r') as file:
    for line in file:
        index = int(line)
        if num > index >= -num:
            result *= some_list[index]
print(result)


# 2й вариант

# import random

# num = int(input('Введите целое число N: '))
# new_list = [random.randint(-num, num) for r in range(num)]
# index_list = []
# prod = 1
# with open('indexes.txt', encoding='UTF-8') as data: #указать кодировку записи
#     for index in data:
#         index_list.append(int(index))
# for i in range(-num, num):
#     if i in index_list:
#         prod *= new_list[i]
# print(prod)