#"""
#Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

#Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
#Вывод: значение типа <list>

#Пример:
#[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
#[2, 4, 6, 8]
#"""

n = list("1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9")

list = n
print(list)

list_count = []
for i in list:
    count = 0
    for k in list:
        if k == i:
            count += 1
    list_count.append(count)
print(list_count)

result = []
for i in range(len(list_count)):
    if list_count[i] == 1:
        result.append(list[i])
print(result)
