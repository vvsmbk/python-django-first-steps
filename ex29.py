# Алгоритм Эвклида
# даны два простых числа а и б, нужно определить НОД для них.
# вариант 1: Из большего числа вычтем меньшее значение и результат запишем в
# переменную с большим значением (и так до тех пор, пока не получим общий делитель)
# пока а != б
#       находим большее среди а и б
#       уменьшаем большее на величину меньшего
import time


def get_nod(a, b):
    """
    Вычисление НОД для натуральных чисел по алгоритму Эвклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def test_nod(func):
    """
    Тестирует функцию, вычисляющую НОД, на правильность работы
    :param func:  функция
    :return: None
    """
    # Test 1
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    # Test 2
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    # Test 3
    a = 2
    b = 10000000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


a = 18
b = 24
res = get_nod(a, b)
# test_nod(get_nod)
print(res)
help(test_nod)
help(get_nod)  # выводит описание функции, записанное в комментарии выше


# Вариант 2: b = b % a = 0:
# a = 18, b = 24
# b = 24 % 18 = 6
# a = 18 % 6 = 0

def get_nod(a, b):
    """
    Вычисление НОД для натуральных чисел по быстрому алгоритму Эвклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


a = 18
b = 24
res = get_nod(a, b)
test_nod(get_nod)
print(res)
