import pyinputplus as pyin
import re
import random

treasure_location = [random.randint(0,2), random.randint(0,2)]
treasure_map = [ ['X','X','X'],['X','X','X'],['X','X','X']]
def draw_map():
    x = 0
    y = 0
    map_size = len(treasure_map)
    for x in range(map_size):
        for y in range(map_size):
            print("|" + treasure_map[x][y], end="")
            if y == map_size - 1:
                print("|")

def guessMap():
    map_size = len(treasure_map) - 1
    regex = f"[0-{map_size}+[:]+[0-{map_size}]"
    guessRe = re.compile(regex)

    while True:
        guess = pyin.inputStr("Please enter [Digit]:[Digit]")
        if re.match(guessRe, guess):
         return guess
        else:
            print("You did not enter the correct sequence")

def checkWin(x,y):
    if x == treasure_location[0] and y == treasure_location[1]:
        print("You win!")
        treasure_map[x][y] = 'T'

        draw_map()
        return True
    else:
        return False

draw_map()
print("Where is the treasure? Input coordinates (Example 1:1/ 0:1): ")

guesses = 0
while True:
    guess = guessMap()
    x_coord = int(guess[0])
    y_coord = int(guess[2])
    if(checkWin(x_coord,y_coord) == False):
        treasure_map[x_coord][y_coord] = 'O'
        draw_map()
        print("Where is the treasure? Input coordinates (Example 1:1/ 0:1): ")
        guesses += 1
        if(guesses == 1):
            print(f"You have guessed {guesses} time.")
        else:
            print(f"You have guessed {guesses} times")

    else:
        break




