words = ["Donkey", "Dog", "Cat", "Monkey", "Elephant"]

with open("file5.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word , "#"*len(word))

with open("file5.txt", "w") as f:
    f.write(content)