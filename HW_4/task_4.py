#"""
#Даны файлы, в каждом из которых находится запись многочлена.
#Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
#Входными данными для этой задачи являются выходные данные их предыдущей.

#Ввод: значения типа <str>, полученные из файлов.
#Вывод: значение типа <str>, файл с одной строкой.

#Примеры:
#9x^5+7x^4+7x^3+9x^2+6x+17=0
#3x^2+2x+1=0
#9x^5+7x^4+7x^3+12x^2+8x+18=0
#"""

import unittest

from task_4 import < '{list_of_poly_1} + {list_of_poly_2}' > as target


# Класс с тестами
class TestClass(unittest.TestCase):

def test_sum_poly(self):
with open('poly_1.txt', 'w', encoding='test_task_4.ru') as file:
    file.write('9x^5+7x^4+7x^3+9x^2+6x+17=0')
with open('poly_2.txt', 'w', encoding='test_task_4.ru') as file:
    file.write('3x^2+2x+1=0')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='test_task_4.ru') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')

        # Если ваши полиномы не имеют пробелов, то уберите их в строках ниже.
        #poly_1 = '9x^5+7x^4+7x^3+9x^2+6x+17=0'
        #poly_2 = '3x^2+2x+1=0'

     
       # self.assertEqual(target(poly_1, poly_2), expect)


if __name__ == '__main__':
    unittest.main()