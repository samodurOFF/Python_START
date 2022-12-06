"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?
N % (k + 1)

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

from random import randrange


def player_player():
    """Игра на 2 игрока"""
    n = randrange(100, 500)
    k = randrange(10, 30)
    name_0 = "Игрок 1"
    name_1 = "Игрок 2"
    order = bool(randrange(2))
    game = True

    while game:
        candy_max = k if k < n else n
        print(f"Ход делает {name_1 if order else name_0}")
        print(f"На столе {n} конфет")
        print(f"Можно взять от 1 до {candy_max}")

        while True:
            m = int(input("Введите количество конфет "))
            if 1 <= m <= candy_max:
                break
            else:
                print("Не верное количество")
                print(f"Можно взять от 1 до {candy_max}")

        n -= m
        if n:
            order = not order
        else:
            game = False
        print()
    print(f"Выиграл {name_1 if order else name_0}")


def player_bot():
    """Игра с тупым ботом"""
    n = randrange(100, 500)
    k = randrange(10, 30)
    name_0 = "Игрок 1"
    name_1 = "Тупой БОТ"
    order = bool(randrange(2))
    game = True

    while game:
        candy_max = k if k < n else n
        print(f"Ход делает {name_1 if order else name_0}")
        print(f"На столе {n} конфет")
        print(f"Можно взять от 1 до {candy_max}")

        if order:
            m = randrange(1, candy_max + 1)
            print(f"Бот взял {m} конфет")
        else:
            while True:
                m = int(input("Введите количество конфет "))
                if 1 <= m <= candy_max:
                    break
                else:
                    print("Не верное количество")
                    print(f"Можно взять от 1 до {candy_max}")

        n -= m
        if n:
            order = not order
        else:
            game = False
        print()
    print(f"Выиграл {name_1 if order else name_0}")


def player_smart_bot():
    """"Игра с умным ботом"""
    n = randrange(100, 500)
    k = randrange(10, 30)
    name_0 = "Игрок 1"
    name_1 = "Умный БОТ"
    order = bool(randrange(2))
    game = True

    while game:
        candy_max = k if k < n else n
        print(f"Ход делает {name_1 if order else name_0}")
        print(f"На столе {n} конфет")
        print(f"Можно взять от 1 до {candy_max}")

        if order:
            x = n % (candy_max + 1)
            m = x if x else 1
            print(f"Бот взял {m} конфет")
        else:
            while True:
                m = int(input("Введите количество конфет "))
                if 1 <= m <= candy_max:
                    break
                else:
                    print("Не верное количество")
                    print(f"Можно взять от 1 до {candy_max}")

        n -= m
        if n:
            order = not order
        else:
            game = False
        print()
    print(f"Выиграл {name_1 if order else name_0}")


def bot_bot():
    """Битва ботов"""
    n = randrange(100, 500)
    k = randrange(10, 30)
    name_0 = "Умный БОТ 1"
    name_1 = "Умный БОТ_2"
    order = bool(randrange(2))
    game = True
    m = 0

    while game:
        candy_max = k if k < n else n
        print(f"Ход делает {name_1 if order else name_0}")
        print(f"На столе {n} конфет")
        print(f"Можно взять от 1 до {candy_max}")

        if order:
            x = n % (candy_max + 1)
            m = x if x else 1
            print(f"Бот 2 взял {m} конфет")
        else:
            x = n % (candy_max + 1)
            m = x if x else 1
            print(f"Бот 1 взял {m} конфет")

        n -= m
        if n:
            order = not order
        else:
            game = False
        print()
    print(f"Выиграл {name_1 if order else name_0}")


if __name__ == '__main__':
    # player_player()
    # player_bot()
    # player_smart_bot()
    bot_bot()
