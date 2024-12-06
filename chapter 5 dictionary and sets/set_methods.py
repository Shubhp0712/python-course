s = {23,32,11,14,43,70,2,1,7}
print("Initial set :", s)

s.add(5) # adds an element to the set. If the element is already present, the add() method will not add the element.
print("Set after adding 5 :", s) #it will add 5 in set at any position because set is unindexed.

s.remove(7) # removes the specified element from the set. If the element is not present, it will raise an error.
print("Set after removing 7 :", s)

s.discard(25) # removes the specified element from the set. If the element is not present, it will not raise an error.
s.discard(23)
print("Set after discarding :", s) 

s.pop() # removes the last element from the set. If the set is empty, it will raise an error.
print("Set after pop :", s)

s.clear() # removes all the elements from the set.
print("Set after clear :", s)  # it will print an empty set.