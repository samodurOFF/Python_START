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

n = int(input('Введите число: '))


def Fibonacci(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def NegaFibonacci(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return Fibonacci(n)*((-1)**(n+1))



Fibonacci_number = []
for n in range(0, n+1):
    Fibonacci_number.append(Fibonacci(n))
    Fibonacci_number.insert(0, NegaFibonacci(n))

    
print(Fibonacci_number)