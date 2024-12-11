st = "Shubh is very smart and intelligent."

f = open("filewrite.txt", "w") # open file in write mode. If file not found, it will create file.
f.write(st)

f.close()