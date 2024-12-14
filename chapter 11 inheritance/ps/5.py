class vector:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        return vector(self.a + other.a, self.b + other.b, self.c + other.c)
    
    def __mul__(self, other):
        result = (self.a * other.a + self.b * other.b + self.c * other.c)
        return result

    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"
    
a = vector(5,7,6)
b = vector(2,8,1)
c = vector(3,4,5)

print(f"The addition of vectors {a} and {b} is {a+b}")
print(f"The multiplication of vectors {a} and {b} is {a*b}")

print(f"The addition of vectors {a} and {c} is {a+c}")
print(f"The multiplication of vectors {a} and {c} is {a*c}")

print(f"The addition of vectors {b} and {c} is {b+c}")
print(f"The multiplication of vectors {b} and {c} is {b*c}")