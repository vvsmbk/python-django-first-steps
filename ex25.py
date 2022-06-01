# set comparison
seta = {1, 2, 3, 4}
setb = {3, 4, 5, 6, 7}
print(seta & setb)  # пересечение множеств, при этом они остаются без изменения
print(seta.intersection(setb))  # тоже пересечение
seta.intersection_update(setb)  # пересечение, результирующее множество
                                # записывается в seta
print(seta)
setc = {9, 10, 11}
print(setb | setc)      # объединение множеств
print(setb.union(setc))  # тоже объединение
seta = {1, 2, 3, 4}
print(seta - setb)      # остаются те элемены, которые только в А, но не в Б
print(setb - seta)      # остаются те элемены, которые только в Б, но не в А
print(seta ^ setb)      # операция симметричной разности (общие элементы исключены)
seta = {7, 6, 5, 4, 3}
setb = {3, 4, 5, 6, 7}
print(seta == setb)     # множества равны, если и длина , и значения совпадают
print(seta != setb)     # проверка на неравенство
seta = {7, 6, 5, 4, 3}
setb = {3, 4, 5}
print(setb < seta)      # множество Б входит в множество А?

#################################################
# 6.5.1
# s1 = set(map(int, input().split()))
# s2 = set(map(int, input().split()))
# s3 = set()
# for a in s1:
#     for b in s2:
#         if a == b:
#             s3.add(a)
# print(*sorted(s3))
# 6.5.2
# s1 = set(map(int, input().split()))
# s2 = set(map(int, input().split()))
# s3 = set()
# for a in s1:
#     if a not in s2:
#         s3.add(a)
# print(*sorted(s3))
# 6.5.3
# s1 = list(map(int, input().split()))
# s2 = list(map(int, input().split()))
# lst = s1 + s2
# s3 = set()
# for x in lst:
#     if lst.count(x) == 1:
#         s3.add(x)
# print(*sorted(s3))
# 6.5.4
# s1 = set(input().split())
# s2 = set(input().split())
# print("ДА" if (s1 >= s2 or s2 >= s1) else "НЕТ")
# 6.5.5
# s = set(map(int,input().split()))
# if 2 in s:
#     print("НЕ ДОПУЩЕН")
# else:
#     print("ДОПУЩЕН")
# 6.5.6
# s1 = set(input().split())
# s2 = set(input().split())
# print("ДА" if (s1 >= s2 or s2 >= s1) else "НЕТ")
# 6.5.7
# n = int(input())
# [print("ДА") if n % 30 == 0 else print("НЕТ")]