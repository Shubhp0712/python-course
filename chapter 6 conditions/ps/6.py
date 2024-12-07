marks = int(input("Enter your marks: "))

# if marks in range(90,100):
#     print("Grade EX")

# elif marks in range(80,90):
#     print("Grade A")

# elif marks in range(70,80):
#     print("Grade B")

# elif marks in range(60,70):
#     print("Grade C")

# elif marks in range(50,60):
#     print("Grade D")

# else:
#     print("Grade F")


# Another way to solve this problem.

if(marks>=90 and marks<=100):
    print("Grade EX")

elif(marks>=80 and marks<90):
    print("Grade A")

elif(marks>=70 and marks<80):
    print("Grade B")

elif(marks>=60 and marks<70):
    print("Grade C")

elif(marks>=50 and marks<60):
    print("Grade D")

else:
    print("Grade F")
    