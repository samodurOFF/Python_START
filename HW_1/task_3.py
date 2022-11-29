"""
Напишите программу, которая принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Ввод: два значения типа <int>
Вывод: значение типа <int> либо значение типа <str>

Пример:

34
-30
4

2
4
1

-34
0
Точка на отрицательной части оси абсцисс
"""

x = int(input('Введите координату точки X: '))
y = int(input('Введите координату точки Y: '))

if y != 0:
    if x > 0:
        if y > 0:
            print(1)
        elif y < 0:
            print(4)
    elif x < 0:
        if y > 0:
            print(2)
        elif y < 0:
            print(3)
    elif x == 0:
        if y < 0:
            print('Точка на отрицательной части оси ординат')
        else:
            print('Точка на положительной части оси ординат')
else:
    if x < 0:
        print('Точка на отрицательной части ос абсцисс')
    else:
        print('Точка на положительной части ос абсцисс')
