"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
import random
new_list = [round(random.uniform(1, 99), 2)
            for r in range(int(input('Введите размер списка: ')))]
dec_list = []
for i in range(len(new_list)):
    num = str(new_list[i]).split('.')
    if 1 == len(num[-1]):
        dec_list.append(int((num[-1])+'0'))
    else:
        dec_list.append(int(num[-1]))
print(new_list)
print(max(dec_list) - min(dec_list))
