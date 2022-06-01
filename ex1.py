#variables, assgnment operators, 'type' and 'id'
#variables names must:
#1. Be a noun
#2. Reflect the data meaning
#3. First symbols can be a-z, A-Z, '_', next ones can be numbs and letters
#to find keywords open Python Console and print 'help'. Then print 'keywords'

a = 7
print(a)
a = 6.8
print(a)
a = "Hello, World!"
print(a)

a = b = c = "Hi"
print(a, b, c)
#returns object's id, which refers to that variable
print(id(a), id(b), id(c))

a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)
b = 2.2
x = True
#returns type of the variable
print(type(a), type(c), type(b), type(x))