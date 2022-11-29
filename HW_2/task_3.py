#"""
#Задайте список размерностью N. Каждый элемент списка вычисляется выражением (1 + 1 / n) ** n,
#где n – позиция (не индекс) элемента в списке, причем 1 < n < N.
#Выведите сумму элементов списка. Ответ округлите до сотых.

#Ввод: значение типа <int>
#Вывод: значение типа <float>

#Пример:
#1
#2.0

#2
#4.25

#3
#6.62
#"""

def in_list(n):
    list = []
    for i in range (1, n+1):
        list.append((1+1/i)**i)
    return list

def sum(list):
    sum=0
    for i in range (len(list)):
        sum=sum + list[i]
    return sum

n = int(input('Введите число N: '))

list = in_list(n)
print(list)
result = sum(list)
print(result)