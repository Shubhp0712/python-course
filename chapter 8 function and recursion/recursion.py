# Here i want to calculate the factorial of a number using recursion.

# The formula of factorial is:
# factorial(n) = n * factorial(n-1) if n > 0. Here we are calling the function itself.

def factorial(n):
    if(n==0 or n==1):
        return 1
    
    else:
        return n * factorial(n-1) # Here we are calling the function itself.
    

num = int(input("Enter the number: "))
print(f"The factorial of {num} is {factorial(num)}")