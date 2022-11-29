#"""
#Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
#Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
#Решение должно работать при любом натуральном N.

#Ввод: значение типа <int>
#Вывод: значение типа <int>
#"""

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)