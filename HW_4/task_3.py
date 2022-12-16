"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""
import random


def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0,101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    

def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))