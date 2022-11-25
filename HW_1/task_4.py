"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
в этой четверти (x и y).

Ввод: значение типа <int>
Вывод: значение типа <str>

Пример:

3
x < 0, y < 0
"""

quarter_number = int(input("Введите номер четверти: "))

if quarter_number == 1:
    print("x > 0; y > 0")
elif quarter_number == 2:
    print("x < 0; y > 0")
elif quarter_number == 3:
    print("x < 0; y < 0")
elif quarter_number == 4:
    print("x > 0; y < 0")
else:
    print("Невалидный номер четверти")
