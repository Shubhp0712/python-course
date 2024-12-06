s = set()

s.add(20)
s.add(20.0)
s.add('20') 

print("Initial set :", s)

print("Length of set :", len(s)) # it will print 2 because 20 and 20.0 are same but '20' is different from 20 and 20.0. So, it will count 20 and 20.0 as 1.

# the len function is supportes by set, list, tuple, dictionary, string. It will return the length of the object.
