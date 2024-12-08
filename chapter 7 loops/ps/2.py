l = ["Harry", "Soham", "Sachin", "Rahul"]

i = 0

while(i<len(l)):
    
    if(l[i].startswith("S")):
        print("Good morning ",l[i])
    i += 1


# The above code can be written as using for loop as follows:
for name in l: 
    if(name.startswith("S")):
        print("Good morning ",name)