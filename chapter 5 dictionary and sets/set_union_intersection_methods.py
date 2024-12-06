s1 = {5,7,8,2}
s2 = {2,3,4,5}
s3 = {5,7}

print("Union of s1 and s2 :", s1.union(s2)) # returns a set containing the union of sets s1 and s2.

print("Intersection of s1 and s2 :", s1.intersection(s2)) # returns a set containing the intersection of sets s1 and s2.

print("Difference of s1 and s2 :", s1.difference(s2)) # returns a set containing the difference between sets s1 and s2.
print("Difference of s2 and s1 :", s2.difference(s1)) # returns a set containing the difference between sets s2 and s1.

print("Symmetric Difference of s1 and s2 :", s1.symmetric_difference(s2)) # returns a set containing the symmetric difference between sets s1 and s2.we can use symmetric difference instead of difference.

print("Is s1 is subset of s2 :", s3.issubset(s1)) # returns True if all elements of set s3 are present in set s1, otherwise False.

print("Is s1 is superset of s2 :", s1.issuperset(s3)) # returns True if all elements of set s3 are present in set s1, otherwise False.

print("Is s1 is disjoint of s2 :", s1.isdisjoint(s2)) # returns True if no elements of set s1 are present in set s2, otherwise False.

print(s1 - s2) # returns a set containing the difference between sets s1 and s2. It is same as difference method.
