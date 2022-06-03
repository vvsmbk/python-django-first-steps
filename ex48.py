# Функция-генератор. Оператор yield
def get_list():
    for x in [1, 2, 3, 4]:
        yield x


a = get_list()  # теперь это ссылка на функцию-генератор
print(a)
# for x in a:  # можно напечатать так все элементы
#     print(x)
print(next(a))
print(next(a))
print(next(a))
print(next(a))  # при следующем вызове возникнет ошибка StopIteration


def get_sred_arif():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)


a = get_sred_arif()
for o in a:
    print(o)


def find_word(f, word):
    g_indx = 0
    for line in f:
        indx = 0
        while indx != -1:
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1


try:
    with open("lesson_54.txt", encoding="utf-8") as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("File not found")
except:
    print("Error file processing")


#########################################################

# Вводится натуральное число N. Необходимо определить
# функцию-генератор с именем get_sum, которая бы возвращала
# текущую сумму чисел последовательности длины N в диапазоне
# целых чисел [1; N]. Например:
# - для первого числа 1 сумма равна 1;
# - для второго числа 2 сумма равна 1+2 = 3
# ....
# - для N-го числа сумма равна 1+2+...+(N-1)+N
# Реализовать функцию-генератор get_sum без использования
# коллекций. Вызывать ее не нужно, только определить.
# N = 10
#
# def get_sum(N):
#     curr = 0
#     for i in range(1, N+1):
#         curr += i
#         yield curr
#
# print(*tuple(get_sum(N)))

# Мы с вами в заданиях несколько раз генерировали
# последовательность чисел Фибоначчи, которая строится по
# правилу: каждое последующее число равно сумме двух
# предыдущих. Для разнообразия давайте будем генерировать
# каждое последующее как сумму трех предыдущих чисел. При этом
# первые три числа равны 1 и имеем такую последовательность:
# 1, 1, 1, 3, 5, 9, 17, 31, 57, ...
# Не знаю, есть ли у нее название, поэтому, в рамках уроков, я
# скромно назову ее последовательностью Балакирева.
# Итак, на вход программы поступает натуральное число N (N > 5)
# и необходимо определить функцию-генератор, которая бы
# возвращала N первых чисел последовательности Балакирева
# (включая первые три единицы).
# Реализуйте эту функцию без использования коллекций (списков,
# кортежей, словарей и т.п.). Вызовите ее N раз для получения
# N чисел и выведите полученные числа на экран в одну строчку
# через пробел.

def get_sum(N):
    lst = []
    for i in range(1, N + 1):
        if i == 1 or i == 2 or i == 3:
            lst.append(1)
            yield lst[i - 1]
        else:
            lst.append(lst[i - 2] + lst[i - 3] + lst[i - 4])
            yield lst[i - 1]


N = 7
print(*tuple(get_sum(N)))

# Вводится натуральное число N (N > 8). Необходимо определить
# функцию-генератор, которая бы выдавала пароль длиной N
# символов из случайных букв, цифр и некоторых других знаков.
# Для получения последовательности допустимых символов для
# генерации паролей в программе импортированы две строки:
# ascii_lowercase, ascii_uppercase (см. листинг ниже), на
# основе которых формируется общий список:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый
# пароль из случайно выбранных символов chars длиной N и
# делать это бесконечно, то есть, вызывать ее можно
# бесконечное число раз. Сгенерировать случайный индекс indx
# в диапазоне [a; b] для символа можно с помощью функции
# randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(a, b)
#  Сгенерируйте с помощью этой функции первые пять паролей
#  и выведите их в столбик (каждый с новой строки).
from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N = 10


def get_pwd(N):
    global chars
    for x in range(5):
        res = ""
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            res += chars[indx]
        yield res


a = get_pwd(N)
for x in a:
    print(x)

# Вводится натуральное число N. Используя строки из латинских
# букв ascii_lowercase и ascii_uppercase:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно
# сформированные email-адреса с доменом mail.ru и длиной в N
# символов. Например, при N=6, получим адрес: SCrUZo@mail.ru
# Для формирования случайного индекса для строки chars
# используйте функцию randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(0, len(chars)-1)
# Функция-генератор должна возвращать бесконечное число таких
# адресов, то есть, генерировать постоянно. Выведите первые
# пять сгенерированных email и выведите их в столбик (каждый
# с новой строки).

from string import ascii_lowercase, ascii_uppercase
import random

chars = ascii_lowercase + ascii_uppercase
random.seed(1)
N = 6


def get_email(N):
    global chars
    while True:
        res = ""
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            res += chars[indx]
        res += "@mail.ru"
        yield res


a = get_email(N)
i = 0
while i != 5:
    print(next(a))
    i += 1

# Определите функцию-генератор, которая бы возвращала простые
# числа. (Простое число - это натуральное число, которое
# делится только на себя и на 1). Выведите с помощью этой
# функции первые 20 простых чисел (начиная с 2) в одну
# строчку через пробел.
# def get_even():
#     i = 0
#     while True:
#         flag = False
#         i += 1
#         for x in range(1, i):
#             if (i % x) == 0:
#                 flag = False
#                 break
#             flag = True
#         if flag is True:
#             yield i
#         else:
#             continue
#
# i = 0
# while i != 20:
#     print(next(get_even()), end=" ")
#     i += 1
