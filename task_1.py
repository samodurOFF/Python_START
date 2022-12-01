"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""

my_List = [1, 2, 3, 4, 5, 6, 7]
list_nech = []
count = 0
for i in my_List:
    if count % 2 == 1:
        list_nech.append(i)
    count += 1
print(list_nech)
sumOfElements = sum(list_nech)
print("Сумма нечетных элементов:", sumOfElements)