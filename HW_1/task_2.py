"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

if not (x or y or z) == (not x and not y and not z):
    print(bool(1))
else:
    print(bool(0))