#bool type, and/or/not, comparison operators
# or - 1 priority
# and - 2 priority
# not - 3 priority (highest)

#y in [-2; 5]
y = 1.85
print(y >= -2 and y <= 5)
print(-2 <= y <= 5) #also

#y not in [-2; 5]
y = 3
print(y < -2 or y > 5)

#not
x = 5
print(x % 2 == 0 or x % 3 == 0)
print(x % 2 != 0 and x % 3 != 0) #also
print(not (x % 2 == 0 or x % 3 == 0)) #also

#each not null number is True, null is False
print(bool(1))
print(bool(-1))
print(bool(0))