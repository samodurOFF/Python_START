

def task1() -> int:
    """ Задача 2: Найдите сумму цифр трехзначного числа. """
    s = input("Задача 2. Введите числа для сложения: ").split(' ')

    result = 0
    for i in s:
        if i.isdigit():
            result += int(i)

    print(result)


def task2():
    """
    Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
    Вместе они сделали S журавликов.
    Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
    а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
    """
    s = input("Задача 2. Введите общее количество журавликов (число, кратное 6): ")
    if not s.isdigit():
        print("Укажите число, кратное 6.")
        return

    s = int(s)

    if s % 6 != 0:
        print("Количество журавликов должно быть кратно 6.")
    else:
        ma = round((s / 3) * 2)
        mi = round(ma / 4)
        print(f"Катя сделала журавликов: {ma}")
        print(f"Петя и Сережа сделали по одинаковому количеству журавликов: {mi}")


def task3():
    """
    Задача 6: Вы пользуетесь общественным транспортом?

    Вероятно, вы расплачивались за проезд и получали билет с номером.
    Счастливым билетом называют такой билет с шестизначным номером,
    где сумма первых трех цифр равна сумме последних трех.

    Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

    Вам требуется написать программу, которая проверяет счастливость билета.
    """
    s = input("Задача 3. Введите номер билета: ")
    s = list(s)

    for _ in s:
        if not _.isdigit():
            print("Номер билета должен содержать 6 цифр и указываться без пробелов.")
            return

    if len(s) != 6:
        print("Номер билета должен содержать 6 цифр.")
        return

    sum1 = sum([int(_) for _ in s[0:3]])
    sum2 = sum([int(_) for _ in s[3:6]])

    if sum1 == sum2:
        print('Счастливый билет!')
    else:
        print('Обычный билет.')


def task4():
    """
    Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
    если разрешается сделать один разлом по прямой между дольками
    (то есть разломить шоколадку на два прямоугольника).

    *Пример:*

    3 2 4 -> yes
    3 2 1 -> no
    """
    n = int(input("Введите число N: "))
    m = int(input("Введите число M: "))
    k = int(input("Введите число K: "))

    if k % n == 0 or k % m == 0 and k < n * m:
        print(f"Ответ: Да, можно отломить одним разломом от шоколадки размером {n}x{m} долек: {k}")
    else:
        print(f"Ответ: Нет, нельзя отломить одним разломом от шоколадки размером {n}x{m} долек: {k}")


if __name__ == '__main__':
    while True:
        try:
            taskN = input("Укажите № задачи от 1 до 4, 0 - выйти: ")

            if taskN in ['exit', 'stop', '0']:
                break

            if not taskN.isdigit():
                break

            taskN = int(taskN)
            if taskN < 1 or taskN > 5:
                break

            if taskN == 1:
                task1()
            if taskN == 2:
                task2()
            if taskN == 3:
                task3()
            if taskN == 4:
                task4()

            print('')
        except KeyboardInterrupt:
            break
