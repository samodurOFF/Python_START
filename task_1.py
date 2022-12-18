"""
Выведите список простых множественных чисел N.
Ввод: значение типа <int>
Вывод: значение типа <список>
Примеры:
20
[2, 2, 5]
38
[2, 19]
"""

from math import sqrt
n = int(input())
for x in range(2, n + 1):
    if all(x % i != 0 for i in range(2, int(sqrt(x)) + 1)):
        print(x, end=" ")
        