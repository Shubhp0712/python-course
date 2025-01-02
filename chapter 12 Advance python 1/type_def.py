num :int = 5 # by type hinting we can use methods of any data type
print(num.bit_length()) # here we can see the methods of int type

name : str = "sarthak"
print(name.capitalize()) # here we can see the methods of str type

def sum(a:int,b:int) -> int:
    return a + b

print(sum(5,6)) # here we can see the methods of int type