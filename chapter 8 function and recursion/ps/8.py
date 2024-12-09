def table(n):
    i = 1
    while(i<=10):
        print(f"{n} x {i} = {n*i}")
        i+=1

num = int(input("Enter the number: "))
table(num)  # Here we are calling the function table.