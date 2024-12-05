l1 = [23,45,1,20,6,2,11,0,9,3,4,5,7,1,10] # list of integers
print("Initial List :",l1)

print(l1.count(1)) # count the number of occurence of 1 in the list

l1.sort() # sort the list
print("Sorted list: ", l1)

l1.reverse() # reverse the list
print("Reversed List: ",l1)

l1.append(100) # append 100 at the end of the list
print("Appended List: ",l1)

l1.insert(2,200) # insert 200 at index 2
print("Inserted List: ",l1)

l1.remove(100) # remove 100 from the list
print("Removed List: ",l1)

l1.pop(2) # remove the element at index 2
print("Popped List: ",l1)

l2 = [4,1,6,3,2,5,7,8,9,0] # list of integers

l1.extend(l2) # extend the list l1 with the list l2
print("Extended List: ",l1)

l1.clear() # clear the list
print("Cleared List: ",l1)

l1 = [23,45,1,20,6,2,11,0,9,3,4,5,7,1,10] # list of integers

print("Index of 4: ",l1.index(4)) # return the index of 4 in the list