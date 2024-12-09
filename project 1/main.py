"""
1. Snake
-1.Water
0. Gun
"""

import random

print("Welcome to Snake, Water, Gun Game.")

while True:
    computer = random.choice([1, 0, -1])

    youstr = input("Enter your choice : Snake for s, Water for w, Gun for g : ")
    youdict = {"s": 1, "w": -1, "g": 0}
    reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

    you = youdict[youstr]

    print(f"You chose {reversedict[you]} \nComputer chose {reversedict[computer]}")

    if you == computer:
        print("Game Draw.")

    else:
        if you == 1 and computer == -1:
            print("You Win.")
        elif you == -1 and computer == 0:
            print("You Win.")
        elif you == 0 and computer == 1:
            print("You Win.")
        elif you == -1 and computer == 1:
            print("You Lose.")
        elif you == 0 and computer == -1:   
            print("You Lose.")
        elif you == 1 and computer == 0:
            print("You Lose.")
        else:
            print("Something went wrong.")

    playagain = input("Do you want to play again? (y/n) : ")
    if playagain == "n":
        break
    else:
        continue

print("Thanks for playing.")