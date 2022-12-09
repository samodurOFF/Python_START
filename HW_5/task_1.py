"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""


# Вариант_1
def del_word_1(text, sym):
    return " ".join(filter(lambda x: not (sym[0] in x and sym[1] in x and sym[2] in x), text.split()))


# Вариант_2
def del_word_2(text, sym):
    return " ".join(filter(lambda x: not all((sym[0] in x, sym[1] in x, sym[2] in x)), text.split()))


# Вариант_2
def del_word_3(text, sym):
    return " ".join(filter(lambda x: not set(x) >= set(sym), text.split()))


if __name__ == '__main__':
    print(del_word_2('автобус, генерал швабра итог арбуз вагон', "абв"))
    print(del_word_2("бамбуковый красный баобабовый синий барбарисовый фиолетовый", "абв"))
