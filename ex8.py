# main string methods
s = "python"
res = s.upper()
print(res)
print(res.lower())

msg = "abrakadabra"
print(msg.count('ra'))  # how often 'ra' is in msg. msg.count(sub[, start[, end]])
print(msg.count('ra', 4))  # how often 'ra' is in msg from 4th character
print(msg.count('ra', 4, 10))  # how often 'ra' is in msg from 4th to 10th (10 NOT include) character
print(msg.find('br'))  # returns index. msg.find(sub[, start[, end]]). If not find returns -1
# direction --------->
print(msg.rfind('br'))  # returns index. msg.rfind(sub[, start[, end]]). If not find returns -1
# direction <---------
print(msg.index('br'))  # works like find, but in bad result returns error
print(msg.replace('a', 'A'))  # replace all 'a' with 'A'.
print(msg.replace('a', ''))  # remove all 'a'.
print(msg.replace('a', 'A', 2))  # replace first 2 'a' with 'A'
print(msg.isalpha())  # returns True if contains ONLY alphabetical chars
print(msg.isdigit())  # returns True if contains ONLY numbs
print(msg.rjust(5))  # insert 5 spaces on the right. msg.rjust(width[, char])
print(msg.rjust(5, '0'))  # insert 5 zeros on the right. msg.rjust(width[, char])
print(msg.ljust(5, '0'))  # insert 5 zeros on the left. msg.ljust(width[, char])
msg = "Ivanov Ivan Ivanovich"
print(msg.split(" ")) # separate string.
digs = "1,  2, 3,4,  5"
d = digs.replace(" ","").split(",")
print(d)
d=", ".join(d) # unite all substrings with splitter ", "
print(d)
print(", ".join(msg.split()))
msg="       dichbich     \n"
print(msg.strip()) # remove all unnecessary symbols from right and left side
print(msg.lstrip()) # remove all unnecessary symbols from left side
print(msg.rstrip()) # remove all unnecessary symbols from right side
