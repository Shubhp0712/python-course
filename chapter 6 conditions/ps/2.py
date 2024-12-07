mark1 = int(input("Enter marks of subject 1: "))
mark2 = int(input("Enter marks of subject 2: "))
mark3 = int(input("Enter marks of subject 3: "))

total_percentage = (mark1+mark2+mark3)/300*100

if (total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You have passed :", total_percentage)

else:
    print("You have failed :", total_percentage)