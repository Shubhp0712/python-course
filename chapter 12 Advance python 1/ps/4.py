a = 2
b = 0

try:
    print(a/b)

except ZeroDivisionError as e:
    print(f"Error: {e}")