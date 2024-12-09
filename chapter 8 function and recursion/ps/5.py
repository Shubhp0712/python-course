# ***
# ** - for n = 3
# *

def pattern(n):
    if(n>0):
        print("*"*n)
        pattern(n-1)

num = int(input("Enter the number: "))
pattern(num)  # Here we are calling the function pattern.