with open("log.txt", "r") as f:
    data = f.read()

    if("python" in data):
        print("Python is present")
    else:
        print("Python is not present")

    print(data)