"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""

num = int(input('Введите число N '))
new_list = []
divisor = 2
while divisor <= num:
    if num % divisor == 0:
        new_list.append(divisor)
        num //= divisor
    else:
        divisor += 1
print(new_list)
