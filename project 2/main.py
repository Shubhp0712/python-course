import random

num = random.randint(1,100)
a = 0
guess = 0

while (a != num):


    #here guess the number between 1 to 100
    a = int(input("Guess the number :"))

    if(a>num):
        print("Lower number please")
        guess = guess + 1
    else:
        print("Higher number please")
        guess = guess + 1

print(f"You have guessed the number {num} in {guess} attempts.")