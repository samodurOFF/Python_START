#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = float(input('Введите координату по оси X: '))
y = float(input('ведите координату по оси Y: '))
if x > 0 and y > 0:
  print('I четверть')
elif x > 0 and y < 0:
  print('IV четверть')
elif x < 0 and y > 0:
  print('II четверть')
elif x < 0 and y < 0:
  print('III четверть')