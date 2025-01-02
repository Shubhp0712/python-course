n = int(input("Enter the number :"))

with open("Tables.txt","w") as f:
    l1 = [i*n for i in range(1, 11)]
    f.write(str(l1))
