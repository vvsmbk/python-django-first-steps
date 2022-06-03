# анонимные функции (lambda)
s = lambda a, b: a + b  # только в одну строчку, нельзя использовать "+-/*...="
print(s(1, 2))
print(s(2, 3))
a = [4, 5, lambda: print("lambda"), 7, 8]
print(a[2])
a[2]()

lst = [5, 3, 0, -6, 8, 10, 1]


def get_filter(a, filter=None):
    if filter is None:
        return a
    res = []
    for x in a:
        if filter(x):
            res.append(x)
    return res


r = get_filter(lst)
print(r)
r = get_filter(lst, lambda x: x % 2 == 0)
print(r)
r = get_filter(lst, lambda x: x > 0)
print(r)


##############################################################

# Объявите анонимную (лямбда) функцию с одним параметром для возведения числа
# в квадрат. Присвойте эту функцию переменной get_sq.
# get_sq = lambda x: x**2

# Объявите анонимную (лямбда) функцию с двумя параметрами для деления одного
# целого числа на другое. Если происходит деление на ноль, то функция должна
# возвращать значение None, иначе - результат деления. Присвойте эту функцию
# переменной get_div. Вызывать функцию не нужно, только задать.
# get_div = lambda x,y: None if (x == 0 or y == 0) else x/y

# Объявите анонимную (лямбда) функцию для вычисления модуля числа (то есть,
# отрицательные числа нужно делать положительными). Вызовите эту функцию для
# введенного числа x: x = float(input())
# Отобразите результат работы функции на экране.
# x = float(input())
# get_abs = lambda x: abs(x)
# print(get_abs(x))

# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей
# строку фрагмента "ra". То есть, функция должна возвращать True, если такой
# фрагмент присутствует в строке и False - в противном случае. Вызовите эту
# функцию для введенной строки s: s = input()
# Отобразите результат работы функции на экране.
# s = input()
# check_ra = lambda s: True if s.count("ra") > 0 else False
# print(check_ra(s))

# В программе задана функция filter_lst (см. программу ниже), которая отбирает
# элементы, переданного ей итерируемого объекта и возвращает сформированный
# кортеж значений. На вход программы поступает список целых чисел, записанных в
# одну строчку через пробел. Вызовите функцию filter_lst для формирования:
# - кортежа из всех значений входного списка (передается в параметр it);
# - кортежа только из отрицательных чисел;
# - кортежа только из неотрицательных чисел (то есть, включая и 0);
# - кортежа из чисел в диапазоне [3; 5]
# Каждый результат работы функции следует отображать с новой строки командой:
# print(*lst)
# где lst - список на возвращенный функцией filter_lst. Для отбора нужных
# значений формальному параметру key следует передавать соответствующие
# определения анонимной функции.
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


lst = list(map(int, "5 4 -3 4 5 -24 -6 9 0".split()))
get_negative = lambda x: True if x < 0 else False
get_positive = lambda x: True if x >= 0 else False
get_in_range = lambda x: True if x in range(3, 6) else False
print(*filter_lst(lst))
print(*filter_lst(lst, get_negative))
print(*filter_lst(lst, get_positive))
print(*filter_lst(lst, get_in_range))