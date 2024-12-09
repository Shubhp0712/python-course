def sum(n):

    if(n>0):
        return n + sum(n-1)
    
    else:
        return 0

num = int(input("Enter the number: "))
print("Sum of numbers from 1 to", num, "is", sum(num))  # Here we are calling the function sum.