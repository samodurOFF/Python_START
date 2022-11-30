# Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

N = int(input('Введите число: '))

def getlist():
    total = 1
    current = 1
    while True:
        total *= current
        yield total
        current = current + 1

f = getlist()
print([next(f) for i in range(N)])