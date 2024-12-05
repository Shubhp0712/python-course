list = ["shubh", 7, 5.78, False, "samarth"] # list with 5 elements. List is mutable. We can change the value of list. In this list 5.78 is a float number.
print(list)

print(list[0])
print(list[1])

print(list[1:4]) # print the elements from index 1 to 3

print(list[1:]) # print the elements from index 1 to the end of the list

print(list[:3]) # print the elements from start to index 2

print(list[-1]) # print the last element

print(list[-3:-1]) # print the elements from index -3 to -2

list[1] = 8 # change the value of index 1 because list is mutable

print(list) # print the updated list

print(type(list[2])) # print the type of element at index 2

