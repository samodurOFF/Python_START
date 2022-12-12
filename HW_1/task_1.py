"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)

Пример:
6
True

7
True

1
False
"""
day = int(input("Введите день недели от 1 до 7: "))

if day < 1 or day > 7:
    print("Некорректное число!")
elif day > 5:
    print(bool(1))
else:
    print(bool(0))