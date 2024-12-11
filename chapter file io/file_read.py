# there are two types of file in python : text file and binary file
# text file: file that can be read and write by human
# binary file: file that can be read and write by computer

# open file
f = open("fileread.txt") # open file.txt in read mode which is default mode. If we want to writ in file we have specify the mode 'w'. if file not found, FileNotFoundError will be raised   
new = f.read()

print(new)

# close file
f.close()