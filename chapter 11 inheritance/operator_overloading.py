class oprovl:
    def __init__(self, a , str):
        self.a = a
        self.str = str

    def __add__(self, other):
        return self.a + other.a
    
    def __sub__(self, other):
        return self.a - other.a
    
    def __mul__(self, other):
        return self.a * other.a
    
    def __truediv__(self, other): # This is used to perform division operation 
        return self.a / other.a 
    
    def __floordiv__(self, other): # This is used to perform floor division operation
        return self.a // other.a
    
    def __mod__(self, other): # This is used to perform modulus operation
        return self.a % other.a
    
    def __pow__(self, other): # This is used to perform power operation
        return self.a ** other.a
    
    def __str__(self): # This is used to print the string
        return f"{self.a} {self.str}"
    
    def __len__(self): # This is used to find the length of the string
        return self.a


a = oprovl(10, "Hello")
b = oprovl(5, "World")

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(a)
print(b)
print(len(a))