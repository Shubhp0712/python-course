class A:

    a = "A"

a = A()
print(a.a)
a.a = 0
print(a.a) # it is an instance variable

print(A.a) # it is a class variable. Which is not changed by the instance variable.