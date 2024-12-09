# to convert the celcuis to fahrenheit

def converter(cels):
    fah  = (cels*(9/5)) + 32

    return fah

cels = float(input("Enter the temperature in celcius: "))

fah = converter(cels)

print(f"The temperature in fahrenheit is: {fah}")