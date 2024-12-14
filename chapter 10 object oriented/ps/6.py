class calculator:
    def __init__(harry,num):
        harry.num = num

    def square(harry):
        print(f"The Square of {harry.num} is {harry.num ** 2}")
    
    def cube(harry):
        print(f"The Cube of {harry.num} is {harry.num ** 3}")
    
    def squareroot(harry):
        print(f"The SquareRoot of {harry.num} is {harry.num ** 0.5}") # Here we are using the power of 0.5 to get the square root of the number.We can also use the math module to get the square root of the number.

n = int(input("Enter the number: "))
a = calculator(n)

a.square()
a.cube()
a.squareroot()