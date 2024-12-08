num = int(input("Enter a number: "))

for i in range(2,num):
    if(num%i==0):
        print(f"Given number {num} is not a prime number")
        break

else:
    print(f"Given number {num} is a prime number")
        