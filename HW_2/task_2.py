"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""

n = int(input("Введите число n: "))
spec_list = []
f = 1
for i in range(1, n+1):
    f = f * i
    spec_list.append(f)
print(spec_list)