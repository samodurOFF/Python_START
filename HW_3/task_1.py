"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""



from random import  randrange
n = int(input('Введите количество элементов: '))
a = [randrange (0, 10) for i in range (n)]
print(a)
def sum_of_position(a):
    sum = 0
    for i in range(len(a)):
        if a[i] % 2 != 0:
            sum += a[i]
    return sum
print(f'Сумма элементов на нечетных позициях равна: {sum_of_position(a)}')


