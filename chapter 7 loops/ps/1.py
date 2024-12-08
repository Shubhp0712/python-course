num = int(input("Enter a number: "))

for i in range(1,11):
    print(num, "x", i, "=", num*i) # this line can be written as print(f"{num} x {i} = {num*i}")
    i += 1

print("The table of", num, "is printed successfully!")