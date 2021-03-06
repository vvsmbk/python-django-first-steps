# List comprehension

# THIS
N = 6
a = [0] * N

for i in range(N):
    a[i] = i ** 2

# CAN BE CHANGED LIKE THIS
N = 6
a = [x ** 2 for x in range(N)]  # [<формированиезначения> for <переменная> in <итерируемый объект>]
print(a)
a = [1 for x in range(5)]
print(a)
a = [1] * N
print(a)
a = [x % 4 for x in range(N+1)]
print(a)
a = [x % 2 == 0 for x in range(N)]
print(a)
a = [0.5 * x + 1 for x in range(N)]
print(a)

# d_inp = input("Integers through space: ")
# a = [int(d) for d in d_inp.split()]
# print(a)
a = [d for d in "python"]
print(a)
a = [ord(d) for d in "python"]
print(a)
a = [x for x in range(-50, 50) if x % 2 == 0 and x % 3 == 0]
print(a)
cities = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Donetsk"]
a = [city for city in cities if len(city) > 4]
print(a)
d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
a = ["четное" if x % 2 == 0 else "нечетное"
     for x in d
     if x > 0]
print(a)

#######################################################################
#Вводятся вещественные числа в строку через пробел. Необходимо на их основе
# сформировать список lst с помощью list comprehension (генератора списков)
# из модулей введенных чисел (в списке должны храниться именно числа, а не
# строки). Результат вывести на экран в виде списка командой:
#print(lst)
#5.56 -8.7 1.0 3.14 77.845
# d = input()
# lst = [abs(float(x)) for x in d.split()]
# print(lst)

# Вводится семизначное целое положительное число. С помощью list comprehension
# сформировать список lst, содержащий цифры этого числа (в списке должны
# быть записаны числа, а не строки). Результат вывести на экран список командой:
#print(lst)
# d = input()
# lst = [int(x) for x in d]
# print(lst)

#Вводится натуральное число N. С помощью list comprehension сформировать
# двумерный список размером N x N, состоящий из нулей, а по главной диагонали
# - единицы. (Главная диагональ - это элементы, идущие по диагонали от верхнего
# левого угла матрицы до ее нижнего правого угла). Результат вывести в виде
# таблицы чисел как показано в примере ниже.
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
# n = int(input())
# lst = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# for r in lst:
#     print(*r)

#Вводятся названия городов в строку через пробел. Необходимо сформировать
# список с помощью list comprehension, содержащий названия длиной более
# пяти символов. Результат вывести в строчку через пробел.
# cities = input().split()
# lst = [cities[i] for i in range(len(cities))
#        if len(cities[i]) > 5]
# print(*lst)

#Вводится натуральное число n. Необходимо сформировать список с помощью
# list comprehension, состоящий из делителей числа n (включая и само число
# n). Результат вывести на экран в одну строку через пробел.
# n = int(input())
# lst = [i for i in range(1, n+1)
#        if n % i == 0]
# print(*lst)

#Вводится натуральное число N. Необходимо сгенерировать
# вложенный список с помощью list comprehension, размером N x N,
# где первая строка содержала бы все нули, вторая - все единицы, третья -
# все двойки и так до N-й строки. Результат вывести в виде таблицы чисел
# как показано в примере ниже.
#0 0 0 0
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# n = int(input())
# lst = [[i for j in range(n)]
#        for i in range(n)]
# for el in lst:
#     print(*el)

#Вводится список вещественных чисел. С помощью list comprehension
# сформировать список, состоящий из элементов введенного списка,
# имеющих четные индексы (то есть, выбрать все элементы с четными
# индексами). Результат вывести на экран в одну строку через пробел.
#8.5 11.3 1.0 -4.5 11.34 6.45
# ns = map(float, input().split())
# lst = [v for i, v in enumerate(ns) if (i+1) % 2 != 0]
# print(*lst)

# Вводятся два списка целых чисел одинаковой длины каждый с новой строки.
# С помощью list comprehension сформировать третий список, состоящий из суммы
# соответствующих пар чисел введенных списков. Результат вывести на экран в
# одну строку через пробел.
# 1 2 3 4 5
# 6 7 8 9 10
# a1 = list(map(int, input().split()))
# a2 = list(map(int, input().split()))
# lst = [a1[i] + a2[i] for i in range(len(a1))]
# print(*lst)

#Вводится список в формате:
# <город 1> <численность населения 1> <город 2> <численность населения 2>
# ... <город N> <численность населения N>
# Необходимо с помощью list comprehension сформировать список lst,
# содержащий вложенные списки из пар:
# <город> <численность населения>
# Численность населения - целое число в тыс. человек.
# s = input().split()
# lst = [[s[i-1], int(s[i])] for i in range(1,len(s),2)]
# print(lst)
