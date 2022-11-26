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
def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Ты ошибся. Вводить надо числа!")
    return a


def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


koordinate = inputKoord(2)
checkCoordinates(koordinate)
