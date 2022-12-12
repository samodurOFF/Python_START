"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""


from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

participant1 = input("Введите имя первого игрока: ")
participant2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {participant1}")
else:
    print(f"Первый ходит {participant2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(participant1)
        counter1 += k
        value -= k
        flag = False
        p_print(participant1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(participant2, k, counter2, value)

if flag:
    print(f"Выиграл {participant1}")
else:
    print(f"Выиграл {participant2}")


# вариант человек против бота:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

participant1 = input("Введите имя первого игрока: ")
participant2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {participant1}")
else:
    print(f"Первый ходит {participant2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(participant1)
        counter1 += k
        value -= k
        flag = False
        p_print(participant1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(participant2, k, counter2, value)

if flag:
    print(f"Выиграл {participant1}")
else:
    print(f"Выиграл {participant2}")



# вариант человек против бота c "интеллектом":
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

participant1 = input("Введите имя первого игрока: ")
participant2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {participant1}")
else:
    print(f"Первый ходит {participant2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(participant1)
        counter1 += k
        value -= k
        flag = False
        p_print(participant1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(participant2, k, counter2, value)

if flag:
    print(f"Выиграл {participant1}")
else:
    print(f"Выиграл {participant2}")