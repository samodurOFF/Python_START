"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.

Ввод: значение типа <int>
Вывод: значение типа <int>

Примеры:
45
101101

3
11

2
10
"""

int_num = int(input("Введите целое число: "))
double_num = ''
while int_num > 0:
    double_elem =int_num % 2
    int_num = int_num // 2
    double_num += str(double_elem) 
print(int(double_num[::-1]))