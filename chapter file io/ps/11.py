with open("file11.txt", "r") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

# This is way to rename a file in python, First we read the content of the file and then write it to a new file with a new name.then we delete the old file.


# Delete the file
import os

os.remove("file11.txt")