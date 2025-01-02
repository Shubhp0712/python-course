# Example of using the walrus operator

# Traditional way
numbers = [1, 2, 3, 4, 5]
n = len(numbers)
if n > 3:
    print(f"The list is too long ({n} elements, expected <= 3)")

# Using the walrus operator
if (n := len(numbers)) > 3:
    print(f"The list is too long ({n} elements, expected <= 3)")