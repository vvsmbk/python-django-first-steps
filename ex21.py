# dict. Basic operations
l = ["car", "house", "tree", "road", "river"]
# {key1: value1, key2: value2, ... keyN: valueN}
d = {"house": "dom", "car": "mashina", "river": "reka"}  # dictionary
print(d)
print(d["river"])
print(dict(one=1, two=3, three='3', four="four"))  # other way to create dict
lst = [[1, "good"], [2, "bad"], [3, "normal"]]
lst = dict(lst)
print(lst[1])

d = {}
d[True] = "True"
d[False] = "False"
print(d)
d = {True: 1, False: "False", 'list': [1, 2, 3], 5: 5}
print(d)
del d[True]
print(d)
print("abc" in d)  # check is d has "abc" key

###############################################################3
# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Значениями здесь являются целые числа (см. пример ниже). Необходимо на их
# основе создать словарь d с помощью функции dict() и вывести его на экран
# командой:
# print(*sorted(d.items()))
# one=1 two=2 three=3
# lst = list(input().split())
# lst = [list(lst[i].split('=')) for i in range(len(lst))]
# for l in range(len(lst)):
#     lst[l][1] = int(lst[l][1])
# d = dict(lst)
# print(*sorted(d.items()))

# Ключами здесь выступают целые числа (см. пример ниже).
# Необходимо их преобразовать в словарь d (без использования
# функции dict()) и вывести его на экран командой:
lst_in = [
    "5=отлично",
    "4=хорошо",
    "3=удовлетворительно"
]
lst_in = [list(lst_in[i].split('=')) for i in range(len(lst_in))]
for l in range(len(lst_in)):
    lst_in[l][0] = int(lst_in[l][0])
d = dict(lst_in)
print(*sorted(d.items()))

# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Необходимо на их основе создать словарь, затем проверить, существуют ли
# в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки). Если
# все они существуют, то вывести на экран ДА, иначе - НЕТ.
# вологда=город house=дом True=1 5=отлично 9=божественно
# lst = list(input().split())
# lst = [list(lst[i].split('=')) for i in range(len(lst))]
# d = dict(lst)
# if 'house' in d and 'True' in d and '5' in d:
#     print("ДА")
# else:
#     print("НЕТ")

# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Необходимо на их основе создать словарь d, затем удалить из этого словаря
# ключи 'False' и '3', если они существуют. Ключами и значениями словаря
# являются строки. Вывести полученный словарь на экран командой:
# lst = list(input().split())
# lst = [list(lst[i].split('=')) for i in range(len(lst))]
# d = dict(lst)
# if 'False' in d:
#     del d['False']
# if '3' in d:
#     del  d['3']
# print(*sorted(d.items()))

#Вводятся номера телефонов в одну строчку через пробел с разными кодами стран:
# +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды
# +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке,
# что и во входной строке) с соответствующими кодами.
# lst = list(input().split())
# for s in lst:
#     lst[lst.index(s)] = ([s[:2], s[2:]])
# d = {}
# for s in lst:
#     if d.get(s[0]) != None:
#         d[s[0]].append(s[1])
#     else:
#         d.update({s[0]:s[1]})
# print(*sorted(d.items()))

#Необходимо создать словарь d, где ключами будут имена, а значениями -
# список номеров телефонов для этого имени. Обратите внимание, что одному
# имени может принадлежать несколько разных номеров.
lst_in = [
["+71234567890", "Сергей"],
["+71234567810", "Сергей"],
["+51234567890", "Михаил"],
["+72134567890", "Николай"]
]
i = 0
while i < len(lst_in):
    lst_in[i].reverse()
    i += 1
d = {}
for s in lst_in:
    if d.get(s[0]) != None:
        d[s[0]].append(s[1])
    else:
        d.update({s[0]:[s[1]]})
print(*sorted(d.items()))

#Пользователь вводит в цикле целые положительные числа, пока не введет число
# 0. Для каждого числа вычисляется квадратный корень (с точностью до сотых)
# и значение выводится на экран (в столбик). С помощью словаря выполните
# кэширование данных так, чтобы при повторном вводе того же самого числа
# результат не вычислялся, а бралось ранее вычисленное значение из словаря.
# При этом на экране должно выводиться: значение из кэша: <число>
# d = {}
# v = 0
# n = -1
# while n != 0:
#     n = int(input())
#     if n == 0:
#         break
#     if d.get(n) != None:
#         print(f"значение из кэша: {d.get(n)}")
#         continue
#     else:
#         v = round(n ** 0.5, 2)
#         d[n] = v
#         print(v)

# d = {}
# v = 0
# n = -1
# while n != 0:
#     n = int(input())
#     if n == 0:
#         break
#     if d.get(n) != None:
#         print(f"значение из кэша: {d.get(n)}")
#         continue
#     else:
#         v = round(n ** 0.5, 2)
#         d[n] = v
#         print(v)