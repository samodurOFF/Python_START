"""
Задайте список размерностью N. Каждый элемент списка вычисляется выражением (1 + 1 / n) ** n,
где n – позиция (не индекс) элемента в списке, причем 1 < n < N.
Выведите сумму элементов списка. Ответ округлите до сотых.

Ввод: значение типа <int>
Вывод: значение типа <float>

Пример:
2
2.0

2
4.25

3
6.62
"""

num = ''
while not num.isdigit():
    num = input('Введите целое число N: ')
    
N = int(num)
some_list = []
for i in range(1, N + 1):
    some_list.append((1 + 1 / i) ** i)
result = sum(some_list)
print(round(result, 2))


# 2й вариант
# n = int(input('ВВедите целое число N: '))
# some_list = round(sum([(1 + 1 / i) ** i for i in range(1, n + 1)]), 2)
# print(some_list)


# 3й вариант
# num = ''
# while not num.isdigit():
#     num = input('Введите целое число N: ')

# N = int(num)
# some_list = []
# for n in range(1, N + 1):
#     some_list.append((1 + 1 / n) ** n)
# sum = 0
# for i in some_list:
#     sum = sum + i
# print(round(sum, 2))
