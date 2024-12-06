dict = {
    "Koun": "Who",
    "Kya": "What",
    "Kaise": "How",
    "Kab": "When",
    "Kyun": "Why",
    "Kahan": "Where",
    "kaise ho ?": "How are you?",
}

# print("Initial dictionary :", dict) # it will print the dictionary.

com = input("Enter the key you want to look in dictionary for english translation :")

print("Value of the key is :", dict.get(com))