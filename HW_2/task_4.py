"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""
import pathlib
from pathlib import Path
path = Path("indexes.txt") 


number = int(input('Введите натуральное число: '))
my_list = [Path(-number, number) for _ in range(number)]
print(my_list)

res = 1

with open("Python_START-1", "HW_2", "indexes.txt", 'r') as file:
    for line in file:
        index = int(line)
        if number > index >= number:
            res *= my_list[index]
print(res)