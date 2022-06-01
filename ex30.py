# Именованные аргументы. Фактические и формальные параметры
def get_V(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    return a * b * c


v = get_V(1, 2, 3)  # позиционная запись аргументов
print(v)

v = get_V(b=1, a=2, c=3)  # именованная запись аргументов
print(v)

v = get_V(1, c=2, b=3)  # комбинированная запись
# (именованные аргументы в конце!)
# и только по порядку: get_V(1, 2, b=3) - ошибка! Аргументу b уже присвоено
# значение 3
print(v)


def get_V(a, b, c, verbose=True):  # verbose - параметр со значением
    # по умолчанию. a,b,c - фактические параметры
    # verbose - формальный. Формальные могут не указываться,
    # а фактические - обязательно указываются как аргументы при вызове
    if verbose:
        print(f"a = {a}, b = {b}, c = {c}")
    return a * b * c


v = get_V(1, 2, 3)
print(v)
v = get_V(1, 2, 3, verbose=False)
print(v)


def cmp_str(s1, s2, reg=False, trim=True):
    if reg:  # переводит в нижний регистр, если true
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:  # удаляет все пробелы, если true
        s1 = s1.strip()
        s2 = s2.strip()

    return s1 == s2  # сравнивает строки


print(cmp_str("Python", " PYTHON", True, True))


def add_value(value, lst=[]):
    lst.append(value)
    return lst


l = add_value(1)
l = add_value(2)
print(l)  # будет два значения, а не 1.
# Это произошло потому, что lst ВСЕГДА ссылается на один и тот
# же список. Так как список не меняется в коде, значения просто
# добавляются в конец.
# чтобы возвращать только один параметр, можно сделать так:
l = add_value(1, [])
l = add_value(2, [])
print(l)


# или так:
def add_value(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst


l = add_value(1)
l = add_value(2)
print(l)
l = add_value(1)
l = add_value(2, l)
print(l)


#####################################################################

# Объявите функцию с именем get_rect_value, которая принимает два аргумента
# (два числа) и еще один формальный параметр type с начальным значением 0.
# Если параметр type равен нулю, то функция должна возвращать периметр
# прямоугольника, а иначе - его площадь.
# P. S. Вызывать функцию не нужно, только объявить.
# def get_rect_value(a, b, type = 0):
#     if type == 0:
#         return 2 * (a + b)
#     else:
#         return a * b

# Объявите функцию с именем check_password, которая принимает аргумент - строку
# (пароль) и имеет один формальный параметр chars с начальным значением в виде
# строки "$%!?@#". Функция должна проверять: есть ли в пароле хотя бы один символ
# из chars и что длина пароля не менее 8 символов. Если проверка проходит, то
# функция возвращает True, иначе - False.
# P. S. Вызывать функцию не нужно, только объявить.
# def check_password(pwd="12345678!", chars="$%!?@#"):
#         s1 = set(pwd)
#         chars = set(chars)
#         if len(pwd) >= 8:
#             if s1 & chars != None:
#                 return True
#             else:
#                 return False
#         else:
#             return False

# print(check_password())


# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее
# в латиницу, используя следующий словарь для замены русских букв на
# соответствующее латинское написание:
t = {'ё': 'yo', '!':'!', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# Функция должна возвращать преобразованную строку. Замены делать без учета
# регистра (исходную строку перевести в нижний регистр - малые буквы).
# У функции также определить формальный параметр sep с начальным значением
# в виде строки "-". Он будет определять символ для замены пробелов в строке.
# После объявления функции прочитайте (с помощью функции input) строку и дважды
# вызовите функцию (с выводом результата ее работы на экран):
# - первый раз только со строкой
# - второй раз со строкой и именованным аргументом sep со значением '+'.

# def str_translation(s, sep='-'):
#     res = ""
#     for l in s.lower():
#         if l == ' ':
#             res += sep
#         else:
#             if set(l) & set(t.values()):
#                 res += l
#             else:
#                 res += t[l]
#     return res
#
# s = input()
# print(str_translation(s))
# print(str_translation(s, '+'))

# Объявите функцию, которая принимает строку и заключает ее в указанный тег.
# Тег определяется формальным параметров tag с начальным значением в виде
# строки "h1". Например, мы передаем строку "Hello Python" и заключаем в тег
# "h1". На выходе должны получить строку (без кавычек):
# "<h1>Hello Python</h1>"
# То есть, сначала открывается тег <h1>, а в конце строки - закрывается </h1>.
# И так для любых указанных тегов.
# После объявления функции прочитайте (с помощью функции input) строку и дважды
# вызовите функцию (с выводом результата ее работы на экран):
#- первый раз только со строкой
#- второй раз со строкой и именованным аргументом tag со значением 'div'.
# def tag_str(s, tag="h1"):
#     if tag == "h1":
#         return "<h1>" + s + "</h1>"
#     else:
#         return "<div>" + s + "</div>"
#
#
# s = input()
# print(tag_str(s))
# print(tag_str(s, "div"))

# Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с
# начальным булевым значением True. Если параметр up равен True, то тег
# (указанный в формальном параметре tag) следует записывать заглавными буквами,
# а иначе - малыми.
# После объявления функции прочитайте (с помощью функции input) строку и дважды
# вызовите функцию (с выводом результата ее работы на экран):
# - первый раз со строкой и именованным аргументом tag со значением 'div'
# - второй раз со строкой, именованным аргументом tag со значением 'div' и
# именованным аргументом up со значением False.
# def tag_str(s, tag="h1", up=True):
#     res = "<h1> </h1>"
#     if tag == "h1":
#         if up == True:
#             return res.upper().replace(' ', s)
#         else:
#             return res.replace(' ', s)
#     else:
#         res = "<div> </div>"
#         if up == True:
#             return res.upper().replace(' ', s)
#         else:
#             return res.replace(' ', s)
#
#
# s = input()
# print(tag_str(s, "div"))
# print(tag_str(s, "div", False))