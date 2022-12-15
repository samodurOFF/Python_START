"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений
Ввод: значение типа <list>
Вывод: три объекта типа <list>
Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
#Вариант а)
from random import random
data = []
for j in range(10):
    data.append(int(random() *10))
print(data)

s = []
for i in data:
    if data.count(i) == 1:
        s.append(i)
print(s)

#Вариант б)
from random import random
data = []
for i in range(10):
    data.append(int(random() *10))
print(data)

b = []
for x in data:
    if data.count(x) > 1:
        b.append(x)
print(b)