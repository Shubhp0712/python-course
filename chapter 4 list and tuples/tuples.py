a = () #here is a empty tuple

b = (1, 2, 3) #here is a tuple with 3 elements

c = (1) #here is a integer because it has only one element and python will consider it as a integer

e = (1,) #here is a tuple with one element

print(type(a))
print(type(b))
print(type(c))
print(type(e))

d = (34,4.56, 3+4j, False, "Shubh") # tuple with 5 elements. Tuple is immutable. We can't change the value of tuple. In this tuple 3+4j is a complex number.

print(d)
print(d[2]) # print the element at index 2
print(type(d[2]))   # print the type of element at index 2
