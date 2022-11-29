"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""

check_predikat = []
for x in range(2):
    for y in True, False:
        for z in True, False:
            check_predikat.append(not (x or y or z) == (not x and not y and not z))
print(all(check_predikat))

# Вариант 2.Решение в строку
# print(all(
#     (not (x or y or z) == (not x and not y and not z) for x in range(2) for y in range(2))
# ))

# Вариант 3
# from itertools import product
# print(all(not (x or y or z) == (not x and not y and not z) for x, y, z in product(*((True, False),) * 3,)))

# мой первый вариант
# def CheckPredikat():
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)
#                 if not (not (x or y or z) == (not x and not y and not z)):
#                     return 'Не для всех значений предикат утверждение истинно'
#     return 'Для всех значений предикат утверждение истинно'
# print(CheckPredikat())
