"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
1 + 2 3 * 4
"""

example = input('Выражение: ').split()
operation = ['*', '/', '+', '-']

while '*' in example:
    ind = example.index('*')
    result = int(example[ind - 1]) * int(example[ind + 1])
    example[ind] = str(result)
    del example [ind + 1]
    del example [ind - 1]
while '/' in example:
    ind = example.index('/')
    result = int(example[ind - 1]) / int(example[ind + 1])
    example[ind] = str(result)
    del example [ind + 1]
    del example [ind - 1]
while '+' in example:
    ind = example.index('+')
    result = int(example[ind - 1]) + int(example[ind + 1])
    example[ind] = str(result)
    del example [ind + 1]
    del example [ind - 1]
while '-' in example:
    ind = example.index('-')
    result = int(example[ind - 1]) - int(example[ind + 1])
    example [ind] = str(result)
    del example [ind + 1]
    del example [ind - 1]    
print(result)