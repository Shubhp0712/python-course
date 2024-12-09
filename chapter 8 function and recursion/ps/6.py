def convert(value):
    if(value > 0):
        return value*2.54
    else:
        return 0
    
num = int(input("Enter the number: "))
print("The value in centimeters is:", convert(num))  # Here we are calling the function convert.