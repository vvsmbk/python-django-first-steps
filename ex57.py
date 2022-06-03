# Битовые операции И, ИЛИ, НЕ, XOR. Сдвиговые операторы
a = 121

print(bin(a))
print(~a) # инверсия числа (битовая операция НЕ)


flags = 5
mask = 4
res = flags & mask  # логическая И
print(res)
if flags & mask == mask:
    print("Включен 2-й бит числа")
else:
    print("2-й бит выключен")

# выключим определённый бит числа
a = 13
b = 5
a = a & ~b
print(a)

# ИЛИ
flags = 8
mask = 5
flags = flags | mask
print(flags)

# Исключающее ИЛИ
flag = 9
mask = 1
flag = flag ^ mask  # XOR
print(flag)
flag = flag ^ mask  # XOR
print(flag)
# Приоритет:
# ~, &, |, ^
# 3, 2, 1, 1

x = 160
print(bin(x))
x = x >> 1      # сдвиг на 1 бит вправо (делим на 2)
print(x)
x = x << 24      # сдвиг на 24 бита влево (умножение на 2^24)
print(x)
# Сдвиговые операции работают сильно быстрее обычного
# умножения и деления


# На вход программы подается целое десятичное число. Используя
# битовые операции, включите третий бит введенного числа.
# Выведите на экран полученное числовое значение.
# P. S. Распределение номеров бит представлено на следующем
# рисунке.
n = 100
print(n | 8)

# На вход программы подается целое десятичное число. Используя
# битовые операции, выключите 4-й и 1-й биты введенного числа.
# Выведите на экран полученное числовое значение.
# P. S. Распределение номеров бит представлено на следующем
# рисунке.
n = 153
print(n & ~18)

# На вход программы подается целое десятичное число. Используя
# битовые операции, переключите 3-й и 0-й биты введенного числа.
# Выведите на экран полученное числовое значение.
# P. S. Распределение номеров бит представлено на следующем
# рисунке.
#n = int(input())
print(n ^ 0b1001)

# На вход программы подается целое десятичное число. Используя
# битовые операции, выполните умножение введенного числа на 4.
# Результат отобразите на экране.
#n = int(input())
print(n << 2)

# На вход программы подается целое десятичное число. Используя
# битовые операции, выполните целочисленное деление введенного
# числа на 2. Результат отобразите на экране.
#n = int(input())
print(n >> 1)

# Вводится зашифрованное слово. Шифрование кодов символов
# этого слова было проведено с помощью битовой операции XOR
# с ключом key=123. То есть, каждый символ был преобразован
# по алгоритму:
# x = ord(x) ^ key
# Здесь ord - функция, возвращающая код символа x. Расшифруйте
# введенное слово и выведите его на экран.
# P. S. Подсказка: для преобразования кода в символ используйте
# функцию chr.
s = "ѩкю[щюлцхZ"
key = 123
res = ""
for x in s:
    c = ord(x) ^ key
    res += chr(c)
print(res)



