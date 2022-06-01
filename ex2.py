#int, float, complex, arithmetical operations
#arithmetical operations:
#+ (2 priority)
#- (2 priority)
#* (3 priority)
#/,// (3 priority)
#% (3 priority)
#** (4 priority)
#NOTE: var '_' in Python Console includes last calculated value

#operation '//' rounds result to the lowest integer
a = 7 // 2
print(a)
a = -7 // 2
print(a)

a = 9 % 5
print(a)
#Найти наименьшее (меньшее -9, ближайшее) кратное 5 (т.е. -10),
#тогда остаток будет -9-(-10)=1
a = -9 % 5
print(a)
#А здесь наоборот берём кратное, которое превышает делимое (т.е. 10),
#тогда 9-10=-1
a = 9 % -5
print(a)
#Когда оба значения отрицательны, то работаем стандартным образом,
#только в области отрицательных значений
a = -9 % -5
print(a)

#'**' operator means exponentiation
#2**3**2 = 512: Firstly multiplies 3*3, then 2^(9)
#Works that way: <-------
a = 2 ** 3 ** 2
print(a)
a = 27 ** 1/3 #(27^1)/3 - incorrect
print(a)
a = 27 ** (1/3) #27^(1/3) - correct
print(a)