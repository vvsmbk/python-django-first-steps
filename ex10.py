# string formatting. 'format' method, F-strings
age = 18
name = "Alex"
print("My name is " + name + " and I\'m " + str(age) + " years old")
print("My name is {0} and I\'m {1} years old".format(name, age))  # str.format(args)
print("My name is {fio} and I\'m {old} years old".format(fio=name, old=age))  # str.format(args)
# F-strings is only in Python 3.6
print(f"My name is {name} and I\'m {age} years old")
print(f"My name is {name.upper()} and I\'m {age} years old")
print(f"My name is {len(name)} and I\'m {age*2} years old")
