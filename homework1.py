"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)
Пример:
6
True
7
True
1
False
"""

day = int(input('Введите от 1 до 7 включительно: '))
if day == 6 or day == 7:
  print('Этот день является выходным')
elif day >= 1 and day <= 8:
  print('Это будний день')
else:
  print('Цифра введена некорректно')