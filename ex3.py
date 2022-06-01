#math operations, math module
a = abs(-1.5) #modulo number
print(a)
a = min(1, 2, 3, 4, 0, -10) #minimal number
print(a)
a = max(1, 2, 3, 4, 0, -10) #maximal number
print(a)
a = pow(2, 3)#exponentiation
print(a)
a = round(1.5) #rounds float number
print(a)
#BUT
a = round(10.5)
print(a)
#ALSO
a = round(7.875543, 2)
print("THIS " + str(a))
#rounds to tens
a = round(7.875543, -1)
print(a)
#rounds to hundrends
a = round(787.5543, -2)
print(a)

import math

#rounds numb to the biggest integer
print(math.ceil(5.2))
print(math.ceil(-5.2))
#rounds numb to the lowest integer
print(math.floor(5.2))
print(math.floor(-5.2))

#returns factorial
print(math.factorial(6))
#discards the fractional part
print(math.trunc(6.5), int(6.5))
#logs
print(math.log2(4), math.log(27, 2), math.log10(1000), math.log(2.7))
#square
print(math.sqrt(49))
#sin, cos, pi, e
print(math.sin(math.pi/2), math.cos(0), math.e)

import math
nominator = math.factorial(6)
print(nominator)
denominator = math.factorial(3)*math.factorial(6-3)
print(denominator)
c = nominator/denominator
print(int(c))

