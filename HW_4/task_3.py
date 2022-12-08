#"""
#Задать натуральное число k.
#Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
#Многочлен вывести в консоль и записать в файл.

#Ввод: значение типа <int>
#Вывод: значение типа <str>, файл с одной строкой.

#Пример:
#2
#2x^2 + 4x + 5 = 0
#"""

from random import randint
import random

k = int(input('Введите число k: '))

result = ''
temp = []
for i in range(k):
    temp.append(randint(0, 100))


znak = ['+', '-']
i = 0
j = 0
while k > 1:
    if temp[i] != 0:
        result += (f'{temp[i]}x**{k}{random.choice(znak)}')
    k -= 1
    i += 1


if temp[-1] != 0:
    result += (f'{temp[-1]}=0')
else:
    result += ('=0')
with open('result.txt', 'w', encoding='test_task_3.ry') as file:
    file.write(f'{temp}\n {result}')

