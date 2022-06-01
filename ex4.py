#print(), input()
#int(), float()

#to remove \n in the end of the strng, type in:
print("Hello", end=" ")
print("World!")

x, y = 5.76, -8
#sep removes spaces after comma
print("Dot coordinates: x = ", x, "; y = ", y, sep="")
#Python 3.6 and later has F-strings:
print(f"Dot coordinates: x = {x}; y = {y}")

a = input()
print(a, type(a))

a = int(input("Insert integer number:"))
print(a, type(a))

a, b = map(int, input("Insert two sides of rectangle:").split())
print("Perimeter: ", 2*(a+b))
