f = open("filefunction.txt") 

# read file
# new = f.readlines() # read all lines of file and return them as list
# print(new, type(new)) 

# new1 = f.readline() # read only one line of file
# print(new1, type(new1))

line = f.readline()

while (line != ""):
    print(line)
    line = f.readline() # read next line. If there is no line to read, it will return empty string. If we don't use this line, it will print infinite time.

# close file
f.close()