"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
'ffffffffffff11111111111      aaaaa'
'9f3f91216 5a'
"""


def my_zip(data):
    res = ""
    temp_sym = ""
    for sym in data:
        if temp_sym:
            if sym in temp_sym and len(temp_sym) < 9:
                temp_sym += sym
            else:
                res += str(len(temp_sym)) + temp_sym[0]
                temp_sym = sym
        else:
            temp_sym = sym
    res += str(len(temp_sym)) + temp_sym[0]
    return res


def my_unzip(data):
    res = ""
    data_lst = list(data)
    for i in range(0, len(data_lst), 2):
        res += int(data_lst[i]) * data_lst[i + 1]
    return res




if __name__ == '__main__':
    # print(my_zip('ffffffffffff11111111111      aaaaa'))
    print(my_unzip("9f3f91216 5a"))
