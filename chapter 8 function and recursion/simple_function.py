# Here we have a simple function that takes two arguments and returns their sum.

# without using function
# a = 10
# b = 20
# c = 30
# sum = a + b + c

# print(sum) # Here if we want to add more numbers then we have to write the same code again and again.

# using function

def add(): # Here we have defined a function called add. This is function definition.
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    sum = a + b + c

    print("The sum of the numbers is: ", sum)

add() # This is function call. Here we can add more numbers by just calling the function again and again.