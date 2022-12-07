"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""

from sympy.abc import x
from sympy import *


def sum_poly(*args):
    res = []
    for argument in args:
        s = argument.replace('x', ' * x').replace('x^', 'x ** ').replace(' = 0', '')
        res.append(collect(s, x))
    return str(sum(res)).replace('*x', 'x').replace('**', '^') + ' = 0'


if __name__ == '__main__':
    results = [
        '31x^2 + 98x + 86 = 0',
        '33x^5 + 82x^4 + 71x^3 + 73x^2 + 82x + 38 = 0'

    ]
    print(sum_poly(*results))
