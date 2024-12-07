# st = input("Enter a string: ")

# if (st == "Make a lot of money"):
#     print("spam")

# elif (st == "buy now"):
#     print("spam")

# elif (st == "subscribe this"):
#     print("spam")

# elif (st == "click this"):
#     print("spam")

# else:
#     print("not spam")

# print("program executed successfully") 

# another way to solve this problem 

m1 = "Make a lot of money"
m2 = "buy now"
m3 = "subscribe this"
m4 = "click this"

st = input("Enter a string: ")

if ((m1 in st) or (m2 in st) or (m3 in st) or (m4 in st)):
    print("spam message")

else:
    print("not spam message")