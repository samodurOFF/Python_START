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

from random import randrange
from os import path, mkdir, chdir

k = int(input("Введите натуральное число k "))
polynom = [randrange(101) for i in range(k + 1)]

str_polynom = ""  # создание полинома
plus = False
for num in polynom:
    if num:
        if plus:
            str_polynom += " + "
        else:
            plus = True

        if k > 1:
            str_polynom += f"{num}x^{k}"
        elif k == 1:
            str_polynom += f"{num}x"
        else:
            str_polynom += f"{num}"
    k -= 1
str_polynom += " = 0"

print(str_polynom)  # Вывод в консоль

if not path.isdir("polynom"):  # Запись в файл
    mkdir("polynom")
chdir("polynom")
i = 0
while True:
    if not path.isfile(f"polynom_{i}.txt"):
        with open(f"polynom_{i}.txt", 'w') as file:
            file.write(str_polynom)
        print(f"Результат записан в файл polynom_{i}.txt")
        break
    else:
        i += 1
