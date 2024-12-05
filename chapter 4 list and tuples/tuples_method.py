b = (3,5,1,7,2,8,4,6,1)
print("Initial Tuple :",b)

print(b.count(1)) # count the number of occurence of 1 in the tuple

print(b.index(1)) # return the index of 1 in the tuple of first occurence

print(len(b)) # return the length of the tuple

print(sorted(b)) # sort the tuple

print(max(b)) # return the maximum element of the tuple

print(min(b)) # return the minimum element of the tuple

print(sum(b)) # return the sum of all elements of the tuple

print(b[2:5]) # return the elements from index 2 to 4. it is called slicing

print("Initial Tuple :",b)

a,b,c,d,e,f,g,h,i,j = (10,5,3,8,2,4,6,7,9,1) # unpacking the tuple
print(a,b,c,d,e,f,g,h,i,j) # print the unpacked elements

t = 1,2,"Shubh",4,5 # tuple packing
print(t) # print the tuple


c = (1,5,3)
d = (8,2,4)

concatenate = c + d
print(concatenate) # concatenate the tuple

concate = d + c # concatenate the tuple
print(concate) # concatenate the tuple
