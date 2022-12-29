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
import random

size = int(input('Введите размерность: '))
new_list = [random.randint(1, 10) for index in range(size)]
list1 = []
list2 = []
list3 = []

for i in range(len(new_list)):
    if new_list.count(new_list[i]) == 1:
        list1.append(new_list[i])

for l in range(len(new_list)):
    if new_list.count(new_list[l]) >= 2:
        if list2.count(new_list[l]) < 1:
            list2.append(new_list[l])

for m in range(len(new_list)):
    if list3.count(new_list[m]) < 1:
        list3.append(new_list[m])
        
print(new_list)
print(list1)
print(list2)
print(list3)