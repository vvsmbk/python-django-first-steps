#indexes and string cuts
s = "Hello python"
print(s[1:3]) #print 1 and 2 chars (without 3rd)
print(s[4:]) #print all from 4th
print(s[:5]) #print all before 5th
print(s[:]) #print all
print(s[2:-2]) #print all from 2nd to pre-pre-last
print(s[2:-2:2])#string[start:stop:step]
print(s[::-1])#print all from end to beginning
print(s[::-2])#print all from end to beginning with step in 2 symbols, last one is first in count
s2 = 'A'+s[1:] #only that way can change char in str
print(s2)
print(s2[-1])
