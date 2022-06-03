# Импорт стандартных модулей. Команды import и from
import math
import time
import pprint

pprint.pprint(locals())  # locals() возвращает все локальные переменные
# (в пределах программы можно воспринимать как глобальные)
# pprint формирует более удобный вывод
a = math.ceil(1.8)
print(a)
print(math.pi)
# Стандартная библиотека: https://docs.python.org/3/library/

# На вход программы подается вещественное число. Необходимо импортировать модуль
# math, вызывать функцию ceil этого модуля для введенного числа и отобразить
# результат на экране.
import math

print(math.ceil(float(input())))

# На вход программы подается вещественное число. Необходимо импортировать только
# одну функцию floor из модуля math, вызывать ее для введенного числа и отобразить
# результат на экране.
from math import floor

print(floor(float(input())))

# В программе имеется функция factorial (см. листинг). В начале программы (до
# определения функции) необходимо из модуля math импортировать функцию с тем же
# именем factorial, используя команду from, но так, чтобы они не "затирали" друг
# друга. Уже объявленную функцию не менять. Выполнять функции не нужно, только
# прописать импорт.
from math import factorial


def factorial(n):
    global factorial
    p = 1
    for i in range(2, n + 1):
        p *= i

    print("my factorial")
    return p


# Из модуля random импортируйте только две функции: seed и randint. Затем, в
# программе выполните их, следующим образом:
# seed(1)
# print(randint(10, 50))
from random import seed, randint

seed(1)
print(randint(10, 50))

# Из модуля random импортируйте только две функции: seed и random, но у последней
# должен быть синоним rnd (имя, через которое она будет вызываться в программе).
# Выполните в программе эти функции, следующим образом:
# seed(10)
# print(round(rnd(), 2))
from random import seed, random as rnd

seed(10)
print(round(rnd(), 2))
