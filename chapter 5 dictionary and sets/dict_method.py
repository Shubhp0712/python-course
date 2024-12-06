marks = {
    "Shubh" : 95,
    "Rudra" : 90,
    "Mir" : 85,
    "Jay" : 99,
    "Samarth" : 92,
}

print("Initial Dictionary :", marks)

print("Items in Dictionary :", marks.items()) # returns a list of a dictionary's key-value pairs in tuple.

print("Keys in Dictionary :", marks.keys()) # returns a list of a dictionary's keys.

print("Values in Dictionary :", marks.values()) # returns a list of a dictionary's values.

marks.update({"Mir" : 97 , "Mark" : 94}) # updating the value of key Mir and also add the marks of Mark. Because dictionary is mutable.

print("Updated Dictionary :", marks)

print(marks.get ("Shubh"),marks.get("sam")) # returns the value of the specified key.Here the difference between get and [] is that get will return None if the key is not present in the dictionary, but [] will raise a KeyError.

marks.pop("Jay" , "defalut") # removes the element with the specified key and returns the value of the key. If the key does not exist, it will return the default value.
print("Dictionary after pop :", marks)

marks.popitem() # removes the last inserted key-value pair. If the dictionary is empty, it will raise a KeyError.
print("Dictionary after popitem :", marks)

marks.clear() # removes all the elements from the dictionary.
print("Dictionary after clear :", marks)