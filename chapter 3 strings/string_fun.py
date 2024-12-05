st1 = "Shubh is very smart."
st2 = "samarth is very intelligent."
st3 = "12345"
st4 = "67890ADC"

# Returns the length of the string
print(len(st1))

# capitalize() method returns the string with first letter capitalized
print(st2.capitalize())

# upper() method returns the string in uppercase
print(st2.upper())

# lower() method returns the string in lowercase
print(st2.lower())

# title() method returns the string in title case
print(st1.title())

# count() method returns the number of occurrences of a substring in the given string
print(st1.count("s"))

# find() method returns the index of the first occurrence of the substring in the given string
print(st1.find("is"))

# replace() method replaces the substring with another substring
print(st1.replace("smart", "brilliant"))

# split() method splits the string into a list of substrings
print(st1.split(" "))
print(st1.split("is"))

# join() method joins the elements of the list with the given string
print(" ".join(["Shubh", "is", "very", "smart."]))

#startswith() and endswith() method returns True if the string starts with the given substring
print(st1.startswith("Shubh"))
print(st1.endswith("smart."))
print(st2.startswith("intelligent."))
print(st2.endswith("samarth"))

#strip() method removes the leading and trailing whitespaces
print("   Shubh is very smart.   ".strip())

#lstrip() and rstrip() method removes the leading and trailing whitespaces left and right side respectively
print("   Shubh is very smart.   ".lstrip())
print("   Shubh is very smart.   ".rstrip())

#isalpha() , isdigit(), isalnum() method returns True if all the characters in the string are alphabets
print(st3.isalpha())
print(st3.isdigit())
print(st4.isalnum())
