l1 = [] 

for i in range(4):
    l1.append(int(input("Enter a number: ")))

if l1[0]>l1[1] and l1[0]>l1[2] and l1[0]>l1[3]:
    print("The number",l1[0],"is the greatest")

elif l1[1]>l1[0] and l1[1]>l1[2] and l1[1]>l1[3]:
    print("The number",l1[1],"is the greatest")

elif l1[2]>l1[0] and l1[2]>l1[1] and l1[2]>l1[3]:
    print("The number",l1[2],"is the greatest")

else:
    print("The number",l1[3],"is the greatest")
