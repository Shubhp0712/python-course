marks = []

# while True:  # infinite loop, here we can use any condition to break the loop. when the condition is true then the loop will break
#     mark = input("Enter a mark: ")
#     if mark == "":
#         break
#     marks.append(int(mark))

# print("Initial List :",marks)

# marks.sort()
# print("Sorted List: ",marks)

#there is another way for this program 

for i in range(6):
    marks.append(int(input("Enter a mark: ")))

print("Initial List :",marks)

marks.sort()
print("Sorted List: ",marks)