"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""
from os import path, chdir, listdir


def parser(polynom):
    if not polynom:
        return {}
    polynom = polynom[:polynom.find("=")]
    map_polynom = map(str.strip, polynom.split("+"))
    dict_polynom = {}  #берем данные которые находятся в выводе строки  засовываем в словарь, куда попадает коэффициент и степень
    for data in map_polynom:
        if "x" in data:
            if "^" in data:
                dict_polynom[int(data[data.find("^") + 1:])] = int(data[:data.find("x")])
            else:
                dict_polynom[1] = int(data[:-1])
        else:
            dict_polynom[0] = int(data)
    return dict_polynom


def sum_polynom(poly1, poly2): # принимаем два полинома, которые мы суммируем 
    res_polynom = parser(poly1) # и далее эти два полинома парсим
    dict_polynom = parser(poly2)
    for key in dict_polynom: # проходим по словарю, и если присутствент множитель в обеих словарях
        val = res_polynom.get(key) # get обращается по ключу, но он не выдает ошибки если ключа нет. Он возвращает элемент,который находится на втором месте 
        if val:
            res_polynom[key] += dict_polynom[key]  # тогда мы их суммируем
        else: # если в одном словаре множителя нет
            res_polynom[key] = dict_polynom[key] # тогда сюда его добавляем
    return create_polynom(res_polynom) # lалее  наш словарь передаем в Ф create_polynom где превращаем в строчку


def create_polynom(dict_polynom):
    new_polynom = ""  # создание полинома
    plus = False
    for key in sorted(dict_polynom)[::-1]:
        if plus:
            new_polynom += " + "
        else:
            plus = True

        if key > 1:
            new_polynom += f"{'' if dict_polynom[key] == 1 else dict_polynom[key]}x^{key}"
        elif key == 1:
            new_polynom += f"{'' if dict_polynom[key] == 1 else dict_polynom[key]}x"
        else:
            new_polynom += f"{dict_polynom[key]}"
    if not new_polynom:
        new_polynom += "0 = 0"
    else:
        new_polynom += " = 0"
    return new_polynom


if __name__ == '__main__': 
    if path.isdir("polynom"):  # Проверка есть ли каталог
        chdir("polynom") # если он есть, тогда переходим в него 
    else: #  если каткалога нет,
        print("Каталог с файлами отсутствует") # выводим на печать сообщение
        exit()
#  Если есть каталог
    res_polynom = "" #  создаем пустую переменную, результирующую полином
    for file_name in listdir(): # проверяем все файлы, которые есть в каталоге
        if "polynom_" in file_name:
            with open(file_name, 'r') as file: # тогда в него заходим и считываем
                str_polynom = file.read()
                print(f"{str_polynom} из файла {file_name}") #Далее эту строчку печатаем
                res_polynom = sum_polynom(res_polynom, str_polynom)
    print(f"Сумма многочленов из файлов: {res_polynom}")

    with open("sum_polynom.txt", 'w') as file:  # Запись в файл
        file.write(str_polynom)
        print("Результат записан в файл sum_polynom.txt")
