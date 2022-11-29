# Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N]. 
# Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс). 
# Решение должно работать при любом натуральном N.

import random

rnd = random.Random()
n_list = []
n = int(input("Введите число N: "))
for i in range(n):
    n_list.append(rnd.randint(-n, n))
print(n_list)

umn = 1
with open('file.txt', 'r') as data:
    for line in data:
        umn *= n_list[int(line.strip())]
print(umn)