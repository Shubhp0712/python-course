# For loop in list:

l1= [2.98,4,"Shubh", False, 4.5, 3+4j]

for i in range(len(l1)):
    print(l1[i])
    print(type(l1[i])) # This will print the type of the element of the list.
print("\n")


#For loop in tuple:

t1 = (2.98,4,"Shubh", False, 4.5, 3+4j)

for i in range(len(t1)):
    print(t1[i])
    print(type(t1[i])) # This will print the type of the element of the tuple.
print("\n")


#For loop in string:

s1 = "Shubham"

for i in range(len(s1)):
    print(s1[i])