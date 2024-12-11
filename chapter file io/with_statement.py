f = open("fileread.txt")
data= f.read()
print(data)
# here we explicitly closing the file
f.close()

# with statement

with open("fileread.txt") as f:
    data = f.read()
    print(data)

# here we are using with statement to open file. It will automatically close the file after the block of code. We don't need to explicitly close the file.