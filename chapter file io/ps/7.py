with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
        
    if("python" in line):
        print("Python is present in line :", lineno)
        break
    lineno += 1
else:
    print("Python is not present")
