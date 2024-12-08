n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n}*{i} = {n*i}")
    i -= 1

print(f"the table of {n} printed successfully")