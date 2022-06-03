# Выражения генераторы
# генератор можно определить без привязки к какой-либо коллекции
# (<формирование значения> for <переменная> in <итерируемый объект>)
# здесь круглые скобки не означают кортеж. Генераторов кортежей
# не существует


a = (x **2 for x in range(6))
print(a)  # а ссылается на генератор
print(next(a)) # как и с обычным итератором, генератор переби-
# рается методом next. Генератор перебирается ТОЛЬКО ОДИН РАЗ.
print(next(a))
print(next(a))
print(next(a))
gen = (x **2 for x in range(6))
for x in gen:
    print(x)

for x in gen:   # больше ничего не будет. Перебирается только один раз
    print(x)

gen = (x ** 2 for x in range(6))
lst = list(gen) # преобразовать в список
print(sum((x **2 for x in range(6))), max(((x **2 for x in range(6)))))

# генераторы по сравнению с обычными коллекции не хранят в
# памяти следующее значение (!)

# lst = list(range(10000000000000000000)) # memoryError
lst = (x for x in range(10000000000000000000))
for i in lst:
    print(i, end=" ")
    if i > 100:
        break
print()
lst = (x for x in range(10, 20))
# len(lst) # object of type 'generator' has no len()
print([lst])
print([list(lst)])

########################################################

# Запишите выражение для генератора, который бы возвращал целые
# числа от 2 до 10 000 с шагом 1 (то есть, 2, 3, 4, ..., 10 000)
# Присвойте этот генератор переменной gen. Вызывать генератор и
# отображать что-либо на экране не нужно, только задать его.
# gen = (x for x in range(2, 10001, 1))

# На вход программы поступают два целых числа a и b (a < b),
# записанные в одну строчку через пробел. На их основе
# запишите генератор для формирования квадратов чисел в
# диапазоне [a; b].
# Преобразуйте этот генератор в кортеж чисел (без использования
# операторов циклов) и присвойте эту коллекцию переменной tp.
# P. S. На экране ничего отображать не нужно, только создать
# кортеж на основе генератора.
# a, b = map(int, input().split())
# tp = tuple((x**2 for x in range(a, b+1)))

# На вход программы поступают два целых числа a и b (a < b),
# записанные в одну строчку через пробел. Определите генератор,
# который бы выдавал модули целых чисел из диапазона [a; b]. В
# цикле выведите первые пять значений этого генератора. Каждое
# значение с новой строки. (Гарантируется, что пять значений
# имеются).
# a, b = map(int, input().split())
# gen = (abs(x) for x in range(a, b+1))
#
# i = 0
# while i != 5:
#     print(next(gen))
#     i += 1

# Вводится целое положительное число a. Необходимо определить
# генератор, который бы возвращал модули чисел в диапазоне
# [-a; a], а затем еще один, который бы вычислял кубы чисел
# (возведение в степень 3), возвращаемых первым генератором.
# Вывести в одну строчку через пробел первые четыре значения.
# (Полагается, что генератор выдает, как минимум четыре
# значения).
# a = int(input())
# gen_abs = (abs(x) for x in range(-a, a+1))
# gen_cube = (x ** 3 for x in gen_abs)
# i = 0
# while i != 4:
#     print(next(gen_cube))
#     i += 1

# Используя символы малых букв латинского алфавита (строка
# ascii_lowercase):
# from string import ascii_lowercase
# запишите генератор, который бы возвращал все сочетания из
# двух букв латинского алфавита. Выведите первые 50 сочетаний
# на экран в строку через пробел.
# Например, первые семь начальных сочетаний имеют вид:
# aa ab ac ad ae af ag
from string import ascii_lowercase
gen = (ascii_lowercase[i]+ascii_lowercase[j] for i in range(len(ascii_lowercase)) for j in range(len(ascii_lowercase)))
i = 0
while i != 50:
    print(next(gen), end=" ")
    i += 1

# Имеется список из названий городов.
# Необходимо записать генератор, который бы используя этот
# список, выдавал 1 000 000 наименований городов по циклу.
# То есть, дойдя до конца списка, возвращался в начало и
# повторял перебор. И так, для выдачи миллиона названий.
# Вывести на экран первые 20 наименований городов с помощью
# генератора в одну строчку через пробел.
from itertools import cycle
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
from itertools import cycle
h = []
for i in cycle(cities):
    print(i, end = " ")
    h.append(i)
    if len(h)==20:
        break

# Имеется график функции f(x) = 0.5x^2 - 2. Необходимо записать
# генератор, который бы выдавал значения этой функции для
# аргумента x в диапазоне [a; b] с шагом 0.01. Величины a, b
# вводятся с клавиатуры в одну строчку через пробел как целые
# числа (a< b). Вывести на экран первые 20 значений функции с
# точностью до сотых, взятых из генератора.
# P.S. Значения функции вычислять командой:
# f(x) = 0.5 * pow(x, 2) - 2.0
# a, b = map(int, input().split())
# gen = (0.5 * pow(x/100, 2) - 2.0 for x in range(a*100, (b+1)*100))
# i = 0
# while i != 20:
#     print(round(next(gen),2), end=" ")
#     i += 1