# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('Введите число: ')
sum_digits = 0
for num in number:
    if num.isdigit():
        sum_digits += int(num)

print(sum_digits)
