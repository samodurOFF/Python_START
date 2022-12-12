"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res



s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")