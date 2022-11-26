"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
в этой четверти (x и y).

Ввод: значение типа <int>
Вывод: значение типа <str>

Пример:

3
x < 0, y < 0
"""

def detect_coordinate_quarter(x,y):
    if((x>0)and(y>0)):
        res="первая четверть"
        print(res)
    if((x<0)and(y>0)):
        res = "вторая четверть"
        print(res)
    if((x<0)and(y<=0)):
        res = "третья четверть"
        print(res)
    if((x>0)and(y<0)):
        res = "четвертая четверть"
        print(res)
    return res
  
 def detect_coordinate_range(x):
    if(x == 1):
        res="(x>0)and(y>0)"
        print(res)
    if(x == 2):
        res = "(x<0)and(y>0)"
        print(res)
    if(x == 3):
        res = "(x<0)and(y<=0)"
        print(res)
    if(x == 4):
        res = "(x>0)and(y<0)"
        print(res)
    return res
  
  detect_coordinate_range(3)
  
