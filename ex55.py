# Функции all и any. Примеры их использования


a = [True, True, True, True]
b = all(a)  # если все значения а = True, то True иначе False
print(b)
a = [True, True, False, True]
b = all(a)  # если все значения а = True, то True иначе False
print(b)

a = [0, 1, 2.5, "", "python", [], [1, 2], {}]
b = all(a)  # перед проверкой все элементы переводятся в bool
print(a, b)  # если 0 и пустых коллекций нет, то True:

a = [1, 2.5, "python", [1, 2]]
b = all(a)
print(a, b)

# any возвращает True, если встретилось хотя бы одно ненулевое:
a = [0, 1, 2.5, "", "python", [], [1, 2], {}]
b = any(a)
print(b, a)
a = [0, 0, 0, 0]
print(any(a), a)


# пример
def true_x(a):
    return a == 'x'


P = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
row_1 = all(map(true_x, P[:3]))
row_2 = all(map(true_x, P[3:6]))
row_3 = all(map(true_x, P[6:]))

col_1 = all(map(true_x, P[::3]))
col_2 = all(map(true_x, P[1::3]))
col_3 = all(map(true_x, P[2::3]))
print(row_1, row_2, row_3, "\n", col_1, col_2, col_3)

N = 10
P = [0] * (N * N)
P[4] = '*'
loss = any(map(lambda x: x == '*', P))
print(loss)


##############################################

# Вводится строка целых чисел через пробел. Необходимо
# определить, являются ли все эти числа четными. Вывести
# True, если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any
# или all.

# lst = list(map(int, input().split()))
# res = all(map(lambda x: x % 2 == 0, lst))
# print(res)

# Вводится строка вещественных чисел через пробел. Необходимо
# определить, есть ли среди них хотя бы одно отрицательное.
# Вывести True, если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any
# или all.

# lst = list(map(float, input().split()))
# res = any(map(lambda x: x < 0, lst))
# print(res)

# Объявить функцию с именем is_string, на вход которой
# поступает коллекция (список, кортеж, множество). Она
# должна возвращать True, если все элементы коллекции строки
# и False - в противном случае.
# Сигнатура функции должна быть, следующей:
# def is_string(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего
# не нужно выводить на экран. Задачу реализовать с
# использованием одной из функций: any или all.

def is_string(lst):
    return all(map(lambda x: type(x) == str, lst))


# Вводятся оценки студента в одну строчку через пробел.
# Необходимо определить, имеется ли в этом списке хотя бы
# одна оценка ниже тройки. Если это так, то вывести на экран
# строку "отчислен", иначе - "учится".
# Задачу реализовать с использованием одной из функций: any
# или all.

# lst = list(map(int, input().split()))
# res = any(map(lambda x: x < 3, lst))
# print("отчислен" if res else "учится")

# Вводится текущее игровое поле для игры "Крестики-нолики"
# в виде следующей таблицы:
# # x o
# x # x
# o o #
# Здесь # - свободная клетка. Нужно объявить функцию с именем
# is_free, на вход которой поступает игровое поле в виде
# двумерного (вложенного) списка. Данная функция должна
# возвращать True, если есть хотя бы одна свободная клетка
# и False - в противном случае.
# Сигнатура функции должна быть, следующей:
# def is_free(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего
# не нужно выводить на экран. Задачу реализовать с
# использованием одной из функций: any или all.
# P. S. Считывание входного списка делать не нужно!!!
# Только определить функцию.
def is_free(lst):
    for x in lst:
        return any(map(lambda y: y == '#', x))
