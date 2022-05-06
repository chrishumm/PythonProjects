import random

theNumber = random.randint(1, 100)
guessedNumber = 0
attempts = 0

print("Please guess a number between 1 and 100")
while True:
    guessedNumber = int(input())

    if guessedNumber > 100 or guessedNumber < 1:
        print("Please enter a number between 1 and 100")
    elif guessedNumber > theNumber:
        print("Choose a lower number!")
    elif guessedNumber < theNumber:
        print("Choose a higher number!")
    else:
        break
    attempts += 1
    
    print("You have guessed " + str(attempts)+1 + " times!")
print("Congratulations! You win the game. It took you " +str(attempts) +" guesses")
