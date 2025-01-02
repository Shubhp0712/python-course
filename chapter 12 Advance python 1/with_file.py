with (
    open("test.txt") as f1,
    open("test2.txt") as f2
):
    print(f1.read())
    print(f2.read())
# f = open("test.txt")
# print(f.read())