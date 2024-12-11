import random

def game():

    print("Welcome to the game!")
    print("You have to guess a number between 1 and 10")
    num = random.randint(1, 11) # random number between 1 and 10
    score = 0
    print("You have 3 chances to guess the number")
    for i in range(1,10):
        guess = int(input("Enter your guess: "))
        if guess == num:
            print("Congratulations! You guessed the number correctly")
            score += (10+num)
        else:
            print("Incorrect guess. Try again")
    
    #now fetch the hi-score from the file
    with open("hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore != ''):
            hiscore = int(hiscore) 
        else:
            hiscore = 0

    print(f"Your score is :{score}")

    #update the hi-score if the current score is greater
    if(score > hiscore):
        with open("hi-score.txt", "w") as f:
            f.write(str(score))
            print("Congratulations! You have set a new hi-score")

    return score  

game()



