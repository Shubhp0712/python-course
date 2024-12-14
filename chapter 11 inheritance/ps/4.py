class complex:

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        return complex(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
    def __mul__(self,other):
        return complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    
c1 = complex(2,3)
c2 = complex(3,4)

print(f"The addition of complex number {c1} and {c2} is {c1+c2} ")

print(f"The multiplication of complex number {c1} and {c2} is {c1*c2} ")