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

num = int(input("Введите число: "))
i = 2 
list = []
old = num
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"{old}  {list}")