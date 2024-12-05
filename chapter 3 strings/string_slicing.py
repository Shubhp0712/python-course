str = "shubh"

print(str[0:3]) # it will print shu
print(str[1:4]) # it will print hub
print(str[0:4]) # it will print shub

#Now the nagetive slicing

print(str[-4:-1]) # it will print hub. It is same as str[1:4]

#Now the slicing with skip value

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str[1:11]) # it will print BCDEFGHIJK 
print(str[1:11:2]) # it will print BDFHJ