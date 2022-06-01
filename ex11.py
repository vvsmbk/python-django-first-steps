# lists. Operators and functions
cities = ["Kyiv", "Lviv", "Odesa"]  # list initialization
marks = [8, 7, 10, 12]  # list initialization
#         indexes: 0, 1, 2, 3
# reverse indexes: -4, -3, -2, -1
print(cities[0], marks[3])
print(f"Average mark is: {(marks[0] + marks[1] + marks[2] + marks[3]) / 4}")
print(marks[-1])  # prints last element
marks[1] = "B+"
marks[0] = 9.5
marks[2] = [10, 11, 12]  # nested list
print(marks)
b = list([True, False])  # creates a COPY of list [True, False] in b
print(b)
b = list("python")  # creates a list of iterable objects
print(b)
print(len(b))  # len() returns length of the list
t = [20, 18, 23, 24.6, 30, 31.1]
print(min(t), max(t))  # returns min and max element in the list
print(sum(t))  # returns sum of elements
print(sorted(t))  # returns sorted ascending list (NEW, NOT A COPY)
print(sorted(t, reverse=True))  # returns sorted descending list (NEW, NOT A COPY)

# lst = list(map(int, input().split()))
# print(lst)

#cities = input().split()
# for city in cities:
#     if city == "Kyiv":
#         print(True)
#
# # or
#
# print(cities.count("Kyiv") != 0)

# a1 = input()
# a2 = input()
# a3 = int(input())
# a4 = float(input())
# book = list(a1, a2, a3, a4)
# del book[2]
# book[1] = "Pushkin"
# book[-1] = book[-1]*2
# print(book)

lst = list(map(str, input().split()))
# lst = sorted(lst, reverse=True)
# print(*lst)
cities = ["K", "S", "X"]
lst = cities + lst
print(*lst)