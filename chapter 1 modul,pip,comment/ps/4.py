import os

# Specify the directory (or leave blank to use the current directory)
directory_path = './Domuments/programming language'

try:
    # List all files and subdirectories
    contents = os.listdir(directory_path)
    print("Contents of the directory:", contents)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access the directory.")
