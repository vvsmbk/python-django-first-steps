# list methods
a = [1, -54, 3, 23, 43, -45, 0]
a.append(100)       # Add new element in the end. 'a = a.append(100)' clears 'a'
print(a)
a.insert(3, [-1000, 2 , 3])  # Inserts new value of existing element
print(a)
a.remove(3)         # removes first incoming of '3'
print(a)
a.pop()             # return removable element. Removes last element, if without args
print(a)
a.pop(3)            # removes element by index
print(a)
a.clear()           # clears a
print(a)
a = [1, 1, -54, 3, 23, 43, -45, 0]
c = a.copy()        # creates a COPY of 'a' list. Similar to c = a[:]
print(id(c), id(a))
print(c.count(1), c.count(3), c.count('a'))  # counts all values similar to argument in c
print(c.index(1))         # returns index of first element wich value similar to arg
print(c.index(-54, 1))     # second arg means index from wich start to search
print('s' in c)     # check is c have value 's'
print(c)
c.reverse()  # reverse list c
print(c)
c.sort()    # sorts c
print(c)
c.sort(reverse=True)    # sorts c desc
print(c)
lst = ["A", "C", "B", "Z", "B", "K", "A"]
print(lst)
lst.sort()  # also sorts alphabetical values
print(lst)
lst.sort(reverse=True)
print(lst)

##################################################
#Вводится строка из целых чисел через пробел.
# Если первое число не равно последнему, то нужно добавить значение True,
# а иначе - значение False.
# Результирующий список lst вывести на экран командой:
#print(*lst)
#Реализовать задачу без использования условных операторов.
#a = list(map(int, input().split()))
#a.append(a[0] != a[-1])
#print(*a)

# Имеется список городов:
# cities = ["Москва", "Казань", "Ярославль"]
# Необходимо вставить во вторую позицию этого списка строку "Ульяновск"
# и вывести список командой:
# print(*cities)
cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, "Ульяновск")
print(*cities)

# Вводится строка с номером телефона в формате:
# +7(xxx)xxx-xx-xx
# Необходимо преобразовать ее в список lst (посимвольно,
# то есть, элементами списка будут являться отдельные символы строки).
# Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы.
# Отобразить полученный список на экране командой:
# print("".join(lst))
#input: +7(912)123-45-67
# lst = list(input())
# lst.remove('+')
# lst[0] = '8'
# lst.remove('-')
# lst.remove('-')
# print("".join(lst))

#В одну строчку через пробел вводятся: имя, отчество и фамилия.
# Необходимо представить эти данные в виде новой строки в формате:
# Фамилия И.О. (Например, Сергей Михайлович Балакирев -> Балакирев С.М.).
# lst = list(input().split())
# str = lst[2] + " " + lst[0][0] + "." + lst[1][0] + "."
# print(str)

#Вводятся целые числа в одну строчку через пробел (не менее четырех).
#Необходимо найти три наименьших числа в этой последовательности чисел и
#вывести их на экран в порядке возрастания. Реализовать программу без
#использования условного оператора.
#8 11 -5 10 -1 0 7

# lst = list(map(int, input().split()))
# lst.sort()
# print(*lst[:3])

#Вводятся целые числа в одну строчку через пробел.
# Необходимо преобразовать их в список lst , затем,
# удалить последнее значение и если оно нечетное,
# то в список (в конец) добавить True, иначе - False.
# Отобразить полученный список на экране командой:
#print(*lst)
#Реализовать программу без использования условного оператора.
#
# lst = list(map(int, input().split()))
# lst.insert(-1, lst[-1] % 2 != 0)
# del lst[-1]
# print(*lst)

# Вводятся оценки студента (числа от 2 до 5) в одну строку через пробел.
# Необходимо определить количество двоек и вывести это значение на экран.
# lst = list(map(int, input().split()))
# print(lst.count(2))

#Вводятся названия рек в одну строчку через пробел.
# Необходимо все их отсортировать по именам (по возрастанию) и
# в отсортированном списке удалить первый элемент.
# Результат отобразить на экране в одну строчку через пробел.
#Лена Обь Волга Дон Енисей
# lst = input().split()
# lst.sort()
# del lst[0]
# print(" ".join(lst))