# Функция filter для отбора значений итерируемых объектов
# filter(func, *iterables) - фильтрация элементов итерированного объекта

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x: x % 2 == 0, a)
print(b)  # b- итерируемый объект
for x in b:
    print(x, end=" ")


def is_even(x):
    d = x - 1
    if d < 0:
        return False

    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True


b = filter(is_even, a)  # простое число или нет
print(tuple(b))

lst = ("Kyiv", "Lviv1", "Dnipro", "Kharkiv2", "Kharkiv")
b = filter(str.isalpha, lst)
print(list(b))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# вложение фильтра в фильтр
b = filter(lambda x: x % 2 != 0, filter(is_even, a))
print(list(b))

###################################################

# Вводятся названия городов в одну строчку через пробел.
# Необходимо определить функцию filter, которая бы возвращала
# только названия длиной более 5 символов. Извлеките первые
# три полученных значения с помощью функции next и отобразите
# их на экране в одну строчку через пробел. (Полагается, что
# минимум три значения имеются).
lst = "Тула Ульяновск Хабаровск Владивосток Омск Уфа".split()
b = filter(lambda x: len(x) > 5, lst)
i = 0
while i != 3:
    print(next(b), end=" ")
    i += 1

# Вводится список предметов в виде списка:
# название_1: вес_1
# ...
# название_N: вес_N
# С помощью функции map, необходимо сначала преобразовать этот
# список строк в кортеж, элементами которого также являются
# кортежи:
# (('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
# А, затем, отфильтровать (исключить) все предметы с весом
# менее 500, используя функцию filter. Вывести на экран список
# оставшихся предметов (только их названия) в одну строчку
# через пробел.
# P. S. Для считывания списка целиком в программе уже записаны
# начальные строчки.
print()
lst_in = ['зонт=1000',
          'палатка=10000',
          'спички=22',
          'котелок=543']

t = tuple(filter(lambda x: False if int(x[1]) < 500 else True, tuple((tuple(x.split('=')) for x in lst_in))))
for x in t:
    print(x[0], end=" ")
print()

# Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
lst = list(map(int, "8 11 0 -23 140 1".split()))
lst = list(filter(lambda x: True if (abs(x) >= 10 and abs(x) <= 99) else False, lst))
print(*lst)


# Саша и Галя коллекционируют монетки. Каждый из них решил
# записать номиналы монеток из своей коллекции. Получилось
# два списка. Эти списки поступают на вход программы в виде
# двух строк из целых чисел, записанных через пробел.
# Необходимо выделить значения, присутствующие в обоих
# списках и оставить среди них только четные. Результат
# вывести на экран в виде строки полученных чисел в порядке
# их возрастания через пробел.
# При реализации программы используйте функцию filter и
# кое-что еще (для упрощения программы), подумайте что.

s1 = set(map(int, "1 5 2 7 10 25 50 100".split()))
s2 = set(map(int, "5 2 3 7 10 25 55".split()))
s = s1 & s2
res = list(filter(lambda x : x % 2 == 0, tuple(s)))
print(*sorted(res))

# Вводится список email-адресов в одну строчку через пробел.
# Среди них нужно оставить только корректно записанные адреса.
# Будем полагать, что к таким относятся те, что используют
# латинские буквы, цифры и символ подчеркивания. А также в
# адресе должен быть символ "@", а после него символ точки "."
# (между ними, конечно же, могут быть и другие символы).
# Результат отобразить в виде строки email-адресов, записанных
# через пробел.
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789_"
def check_email(s):
    global chars
    lst = list(s.split('@'))
    if len(lst) > 2:
        return False
    for x in lst[0]:
        if x not in chars:
            return False
    if lst[1].count('.') == 0 or lst[1].count('.') > 1:
        return False
    return True

s = list("abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com".split())
res = list(filter(lambda x: check_email(x), s))
print(*res)
