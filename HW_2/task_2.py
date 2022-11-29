#"""
#Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

#Ввод: значение типа <int>
#Вывод: значение типа <list>

#Пример:
#4
#[1, 2, 6, 24]
#"""

def get_factorial_list(n):
     fact = 1
     facts = []
     for i in range(1, n+1):
         fact *= i
         facts.append(fact)
     return facts
print(get_factorial_list(N))