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


def next_prime(current):
    """
    Самый простой и неоптимизированный алгоритм нахождения простого числа
    """
    while True:
        current += 1
        k = 0
        for j in range(2, current + 1):
            if current % j == 0:
                k += 1
                if k >= 2:
                    break
        if k == 1:
            return current


n = int(input("Введите натуральное число N "))
mult = 2
res = []
while n > 1:
    if n % mult == 0:
        res.append(mult)
        n //= mult
    else:
        mult = next_prime(mult)
print("Список простых множителей натурального числа N: ", res)
