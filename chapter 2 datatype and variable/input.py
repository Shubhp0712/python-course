# i want to perform some operations and i want to take input from user

a = input("Enter a number: ")
b = input("Enter another number: ")
# i want to add these two numbers
c = a + b
print(c) # it will print the concatenated value of a and b. not the sum of a and b because input() function returns string value

# to get the sum of a and b, we need to convert the input values to integer
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = a + b
print(c) # it will print the sum of a and b
