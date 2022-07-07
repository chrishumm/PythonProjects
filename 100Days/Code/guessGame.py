import pyinputplus as pyin
import random

level = 0

def guessGame(randomNumber, level):
    guesses = level * 2
    while guesses > 0:
        guessedNumber = pyin.inputNum(f"You are on level {level}.\nYou have {guesses} guesses left!\nGuess a number between 1 and 100: ")
        if(guessedNumber > randomNumber):
            print("Lower!")
            guesses-= 1
        elif(guessedNumber < randomNumber):
            print("Higher")
            guesses-= 1
        else:
            print("You win!\n\n")
            return True

while True:
    i = 0
    for i in range(10,0,-1):
        if guessGame(random.randint(0,100), i) == False:
            break
    print(f'You got to level{i}')