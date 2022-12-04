"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
num = int(input('Введите размерность: '))
new_list = [1, 0, 1]
for i in range(num - 1):
    new_list.append(new_list[-1] + new_list[-2])
    new_list.insert(0, new_list[1] - new_list[0])
print(new_list)

  