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
num = int(input('Введите число: '))
result_list = []
i = 2
while i <= num:
    if num % i == 0:
        result_list.append(i)
        num //= i
    else:
        i += 1
if num > 1:
    result_list.append(num)
print(result_list)
