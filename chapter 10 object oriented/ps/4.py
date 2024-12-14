class calculator:
    def __init__(self,num):
        self.num = num

    @staticmethod
    def greet():
        print("Hello")

    def square(self):
        print(f"The Square of {self.num} is {self.num ** 2}")
    
    def cube(self):
        print(f"The Cube of {self.num} is {self.num ** 3}")
    
    def squareroot(self):
        print(f"The SquareRoot of {self.num} is {self.num ** 0.5}") # Here we are using the power of 0.5 to get the square root of the number.We can also use the math module to get the square root of the number.

n = int(input("Enter the number: "))
a = calculator(n)

a.greet()
a.square()
a.cube()
a.squareroot()