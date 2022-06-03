# Функция map. Примеры ее использования
b = map(int, ['1', '2', '3', '4', '5', '3', '4', '5'])
# то же самое, только неудобно
a = (int(x) for x in ['1', '2', '3', '4', '5', '3', '4', '5'])

a = sum(b)  # можно только один раз пройтись по последовательности
print(a)

# print(next(b))
# for x in b:
#     print(x, end=" ")


cities = ["Kyiv", "Lviv", "Odesa", "Dnipro", "Kharkiv"]
b = map(len, cities)
a = list(b)
print(a)
b = map(str.upper, cities)
a = list(b)
print(a)
b = map(lambda s: s[::-1], cities)
a = list(b)
print(a)

##########################################################

# На вход поступает список из вещественных чисел, записанных
# в строку через пробел. С помощью функции map преобразовать
# числа в строке в их вещественное представление и отобразить
# первые три числа. (Полагается, что минимум три вещественных
# числа имеются). Реализовать извлечение чисел через функцию
# next. Результат отобразить в строку через пробел.
s = map(float, "4.35 -10.6 1.0 200.34 0.56".split())
i = 0
while i != 3:
    print(next(s), end=" ")
    i += 1

# На вход поступает строка из целых чисел, записанных через
# пробел. С помощью функции map преобразовать эту строку в
# список целых чисел, взятых по модулю. Сформируйте именно
# список lst из таких чисел. Отобразите его на экране в виде
# набора чисел, идущих через пробел.
m = list(map(lambda x: abs(int(x)), "-5 6 8 11 -10 0".split()))
print(*m)

# Вводится таблица целых чисел. Используя функцию map и
# генератор списков, преобразуйте список строк lst_in (см.
# листинг) в двумерный список с именем lst2D, содержащий целые
# числа.
# Выводить на экран ничего не нужно, только сформировать
# список lst2D на основе введенных данных.
lst_in = [
    '8 11 -5',
    '3 4 10',
    '-1 -2 3',
    '-4 5 6'
]
lst2D = [[int(y) for y in x.split()] for x in lst_in]

# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж
# tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать
# строку в кортеж с именем tp.

s = "house=дом car=машина men=человек tree=дерево"
s_lst = s.split()

tp = tuple(tuple(map(str, x.split('='))) for x in s_lst)
print(tp)

# Вводится строка. Необходимо в ней заменить кириллические
# символы на соответствующие латинские обозначения (без учета
# регистра букв), а все остальные символы - на символ дефиса
# (-). Для этого в программе определен словарь (см. листинг).
# Используя его, запишите функцию map, которая бы выдавала
# преобразованные фрагменты для входной строки. На основе этой
# функции сформируйте строку, состоящую из преобразованных
# фрагментов (фрагменты в строке должны идти друг за другом
# без пробелов). Отобразите результат на экране.
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
s = map(str, "Привет Питон")
res = map(lambda x: t.get(x.lower()) if t.get(x.lower()) is not None else x.lower(), s)
for x in res:
    if x == ' ':
        print('-',end='')
    else:
        print(x, end='')

# Вводятся названия городов в одну строчку через пробел.
# Необходимо определить функцию map, которая бы возвращала
# названия городов только длиной более 5 символов. Вместо
# остальных названий - строку с дефисом ("-"). Сформировать
# список из полученных значений и отобразить его на экране в
# одну строчку через пробел.
s = "Москва Уфа Вологда Тула Владивосток Хабаровск"
res = map(lambda x: x if len(x) > 5 else '-', s.split())
for x in res:
    print(x, end=" ")